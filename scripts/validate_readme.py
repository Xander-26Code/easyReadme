#!/usr/bin/env python3
"""Validate README links, media, sections, and common command claims."""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Any


IGNORE_SCHEMES = (
    "http://",
    "https://",
    "mailto:",
    "tel:",
    "ftp://",
    "irc://",
    "data:",
)

MEDIA_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".svg",
    ".mp4",
    ".mov",
    ".webm",
}


def read_json(path: Path) -> dict[str, Any] | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return None


def load_package_scripts(project: Path) -> dict[str, str]:
    data = read_json(project / "package.json")
    if not data:
        return {}
    return data.get("scripts") or {}


def load_make_targets(project: Path) -> set[str]:
    makefile = project / "Makefile"
    if not makefile.exists():
        return set()
    targets: set[str] = set()
    pattern = re.compile(r"^([A-Za-z0-9_.-]+):(?:\s|$)")
    for line in makefile.read_text(encoding="utf-8", errors="ignore").splitlines():
        match = pattern.match(line)
        if match and not match.group(1).startswith("."):
            targets.add(match.group(1))
    return targets


def strip_fragment(target: str) -> str:
    return target.split("#", 1)[0].split("?", 1)[0]


def is_external(target: str) -> bool:
    return target.startswith(IGNORE_SCHEMES) or target.startswith("#")


def normalize_target(target: str) -> str:
    target = target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    return strip_fragment(target)


def extract_links(markdown: str) -> list[dict[str, Any]]:
    links: list[dict[str, Any]] = []

    markdown_link = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
    markdown_image = re.compile(r"!\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
    html_attr = re.compile(r"""(?:href|src)=["']([^"']+)["']""", re.IGNORECASE)

    for line_no, line in enumerate(markdown.splitlines(), start=1):
        for pattern, kind in [(markdown_image, "image"), (markdown_link, "link")]:
            for match in pattern.finditer(line):
                links.append({"kind": kind, "target": match.group(1), "line": line_no})
        for match in html_attr.finditer(line):
            target = match.group(1)
            kind = "image" if re.search(r"<img\b", line, re.IGNORECASE) or Path(strip_fragment(target)).suffix.lower() in MEDIA_EXTENSIONS else "link"
            links.append({"kind": kind, "target": target, "line": line_no})

    return links


def validate_local_links(markdown: str, readme: Path, project: Path) -> list[dict[str, Any]]:
    problems: list[dict[str, Any]] = []
    base = readme.parent
    for item in extract_links(markdown):
        target = normalize_target(item["target"])
        if not target or is_external(target):
            continue
        if target.startswith("/"):
            candidate = project / target.lstrip("/")
        else:
            candidate = base / target
        if not candidate.exists():
            problems.append(
                {
                    "line": item["line"],
                    "kind": item["kind"],
                    "target": item["target"],
                    "message": "Local README target does not exist.",
                }
            )
    return problems


def extract_headings(markdown: str) -> list[str]:
    headings: list[str] = []
    for line in markdown.splitlines():
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if match:
            heading = re.sub(r"<[^>]+>", "", match.group(2))
            heading = re.sub(r"[^\w\s-]", "", heading, flags=re.UNICODE).strip().lower()
            headings.append(heading)
    return headings


def section_status(markdown: str) -> dict[str, bool]:
    headings = extract_headings(markdown)

    def has_any(*needles: str) -> bool:
        return any(any(needle in heading for needle in needles) for heading in headings)

    return {
        "overview": has_any("overview", "about", "what is"),
        "features": has_any("features", "key features"),
        "quick_start": has_any("quick start", "getting started", "how to use", "installation"),
        "configuration": has_any("configuration", "environment", "env"),
        "usage": has_any("usage", "examples", "demo"),
        "testing": has_any("testing", "tests"),
        "license": has_any("license"),
    }


def extract_code_blocks(markdown: str) -> list[dict[str, Any]]:
    blocks: list[dict[str, Any]] = []
    in_block = False
    language = ""
    start = 0
    lines: list[str] = []

    for line_no, line in enumerate(markdown.splitlines(), start=1):
        fence = re.match(r"^```([A-Za-z0-9_-]*)\s*$", line)
        if fence and not in_block:
            in_block = True
            language = fence.group(1).lower()
            start = line_no
            lines = []
            continue
        if fence and in_block:
            blocks.append({"language": language, "start": start, "end": line_no, "text": "\n".join(lines)})
            in_block = False
            continue
        if in_block:
            lines.append(line)

    return blocks


def shellish_commands(markdown: str) -> list[dict[str, Any]]:
    commands: list[dict[str, Any]] = []
    for block in extract_code_blocks(markdown):
        if block["language"] not in {"", "bash", "sh", "shell", "console", "zsh"}:
            continue
        for offset, raw_line in enumerate(block["text"].splitlines()):
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue
            line = re.sub(r"^\$\s+", "", line)
            commands.append({"line": block["start"] + offset + 1, "command": line})
    return commands


def validate_commands(markdown: str, project: Path) -> list[dict[str, Any]]:
    package_scripts = load_package_scripts(project)
    make_targets = load_make_targets(project)
    package_exists = (project / "package.json").exists()
    make_exists = (project / "Makefile").exists()
    problems: list[dict[str, Any]] = []

    for item in shellish_commands(markdown):
        command = item["command"]
        line = item["line"]

        npm_run = re.match(r"^(npm|pnpm|yarn)\s+run\s+([A-Za-z0-9:_-]+)\b", command)
        if npm_run and npm_run.group(2) not in package_scripts:
            problems.append({"line": line, "command": command, "message": "Package script is not defined in package.json."})
            continue

        npm_direct = re.match(r"^npm\s+(start|test)\b", command)
        if npm_direct and package_exists and npm_direct.group(1) not in package_scripts:
            problems.append({"line": line, "command": command, "message": f"`npm {npm_direct.group(1)}` is not backed by a package.json script."})
            continue

        pnpm_direct = re.match(r"^(pnpm|yarn)\s+(start|test|build|dev)\b", command)
        if pnpm_direct and package_exists and pnpm_direct.group(2) not in package_scripts:
            problems.append({"line": line, "command": command, "message": "Package-manager command is not backed by a package.json script."})
            continue

        make_command = re.match(r"^make\s+([A-Za-z0-9_.-]+)\b", command)
        if make_command and make_exists and make_command.group(1) not in make_targets:
            problems.append({"line": line, "command": command, "message": "Make target is not defined in Makefile."})

    return problems


def todo_count(markdown: str) -> int:
    return len(re.findall(r"\bTODO\b|TODO:", markdown, flags=re.IGNORECASE))


def find_media(markdown: str) -> list[dict[str, Any]]:
    return [
        item
        for item in extract_links(markdown)
        if item["kind"] == "image" or Path(strip_fragment(item["target"])).suffix.lower() in MEDIA_EXTENSIONS
    ]


def validate(readme: Path, project: Path) -> dict[str, Any]:
    markdown = readme.read_text(encoding="utf-8", errors="ignore")
    section_checks = section_status(markdown)
    missing_recommended = [name for name, present in section_checks.items() if not present and name in {"quick_start", "usage", "license"}]
    local_link_problems = validate_local_links(markdown, readme, project)
    command_problems = validate_commands(markdown, project)
    media_items = find_media(markdown)

    warnings: list[str] = []
    if todo_count(markdown):
        warnings.append("README contains TODO markers. Keep them only for intentionally missing facts.")
    if not media_items:
        warnings.append("No README media assets detected. This may be fine for libraries/CLIs, but visual products may benefit from screenshots, GIFs, or video links.")
    if missing_recommended:
        warnings.append(f"Missing recommended section(s): {', '.join(sorted(missing_recommended))}.")

    return {
        "readme": str(readme.resolve()),
        "project": str(project.resolve()),
        "passed": not local_link_problems and not command_problems,
        "sections": section_checks,
        "counts": {
            "links_checked": len([item for item in extract_links(markdown) if not is_external(normalize_target(item["target"]))]),
            "media_items": len(media_items),
            "todos": todo_count(markdown),
            "shell_commands": len(shellish_commands(markdown)),
        },
        "problems": {
            "local_links": local_link_problems,
            "commands": command_problems,
        },
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a README against project facts.")
    parser.add_argument("readme", help="README file to validate.")
    parser.add_argument("--project", default=None, help="Project root. Defaults to README parent.")
    parser.add_argument("--json", action="store_true", help="Print JSON output. This is the default format.")
    args = parser.parse_args()

    readme = Path(args.readme)
    if not readme.exists() or not readme.is_file():
        parser.error(f"README file does not exist: {readme}")

    project = Path(args.project) if args.project else readme.parent
    if not project.exists() or not project.is_dir():
        parser.error(f"Project directory does not exist: {project}")

    result = validate(readme.resolve(), project.resolve())
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
