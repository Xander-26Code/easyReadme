#!/usr/bin/env python3
"""Extract README-relevant facts from a project directory.

This script is intentionally conservative. It reports facts that can be read
from files and leaves writing decisions to the README skill.
"""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Any

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Python < 3.11 fallback
    tomllib = None  # type: ignore[assignment]


IGNORE_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".next",
    ".nuxt",
    ".turbo",
    ".venv",
    "venv",
    "__pycache__",
    "node_modules",
    "dist",
    "build",
    "coverage",
    "target",
    ".idea",
    ".vscode",
}

ASSET_EXTENSIONS = {
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

DOC_FILES = {
    "README.md",
    "README",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "LICENSE",
    "LICENSE.md",
}


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def iter_files(root: Path, max_files: int = 5000) -> list[Path]:
    files: list[Path] = []
    for current_root, dirs, names in os.walk(root):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for name in names:
            path = Path(current_root) / name
            files.append(path)
            if len(files) >= max_files:
                return files
    return files


def read_json(path: Path) -> dict[str, Any] | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return None


def read_toml(path: Path) -> dict[str, Any] | None:
    if tomllib is None:
        return None
    try:
        return tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError):
        return None


def detect_make_targets(path: Path) -> list[str]:
    targets: list[str] = []
    if not path.exists():
        return targets

    target_pattern = re.compile(r"^([A-Za-z0-9_.-]+):(?:\s|$)")
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        match = target_pattern.match(line)
        if match and not match.group(1).startswith("."):
            targets.append(match.group(1))
    return sorted(set(targets))


def parse_env_file(path: Path) -> list[str]:
    names: list[str] = []
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[len("export ") :].strip()
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)\s*=", line)
        if match:
            names.append(match.group(1))
    return sorted(set(names))


def detect_asset_kind(path: Path) -> str:
    name = path.name.lower()
    parent = path.parent.as_posix().lower()
    text = f"{parent}/{name}"
    if any(key in text for key in ["screenshot", "screen-shot", "preview"]):
        return "screenshot"
    if any(key in text for key in ["demo", "recording", "showcase"]):
        return "demo"
    if any(key in text for key in ["logo", "brand", "icon"]):
        return "logo"
    if any(key in text for key in ["avatar", "author", "profile"]):
        return "avatar"
    if any(key in text for key in ["diagram", "architecture", "flow"]):
        return "diagram"
    if any(key in text for key in ["star", "stargazer"]):
        return "star-history"
    return "asset"


def package_json_facts(root: Path) -> dict[str, Any] | None:
    path = root / "package.json"
    data = read_json(path)
    if not data:
        return None

    deps = sorted((data.get("dependencies") or {}).keys())
    dev_deps = sorted((data.get("devDependencies") or {}).keys())
    return {
        "path": rel(path, root),
        "name": data.get("name"),
        "version": data.get("version"),
        "description": data.get("description"),
        "license": data.get("license"),
        "scripts": data.get("scripts") or {},
        "dependencies": deps,
        "devDependencies": dev_deps,
        "engines": data.get("engines") or {},
        "bin": data.get("bin"),
        "repository": data.get("repository"),
        "bugs": data.get("bugs"),
        "homepage": data.get("homepage"),
    }


def pyproject_facts(root: Path) -> dict[str, Any] | None:
    path = root / "pyproject.toml"
    data = read_toml(path)
    if not data:
        return None

    project = data.get("project") or {}
    poetry = (data.get("tool") or {}).get("poetry") or {}
    scripts = project.get("scripts") or poetry.get("scripts") or {}
    dependencies = project.get("dependencies") or poetry.get("dependencies") or []
    return {
        "path": rel(path, root),
        "name": project.get("name") or poetry.get("name"),
        "version": project.get("version") or poetry.get("version"),
        "description": project.get("description") or poetry.get("description"),
        "license": project.get("license") or poetry.get("license"),
        "scripts": scripts,
        "dependencies": dependencies,
    }


def detect_stack(files: list[Path], package: dict[str, Any] | None, pyproject: dict[str, Any] | None) -> dict[str, Any]:
    names = {path.name for path in files}
    paths = {path.as_posix() for path in files}
    deps = set((package or {}).get("dependencies") or [])
    dev_deps = set((package or {}).get("devDependencies") or [])
    all_deps = deps | dev_deps

    stack: dict[str, Any] = {
        "languages": [],
        "frameworks": [],
        "package_managers": [],
        "project_types": [],
    }

    if package:
        stack["languages"].append("JavaScript/TypeScript")
        stack["package_managers"].append("npm")
        if "pnpm-lock.yaml" in names:
            stack["package_managers"].append("pnpm")
        if "yarn.lock" in names:
            stack["package_managers"].append("yarn")
        if {"react", "vue", "svelte", "@angular/core"} & all_deps:
            stack["project_types"].append("frontend")
        if {"express", "fastify", "koa", "hono", "nestjs"} & all_deps:
            stack["project_types"].append("backend")
        if {"next", "nuxt", "@remix-run/react"} & all_deps:
            stack["project_types"].append("fullstack")
        if package.get("bin"):
            stack["project_types"].append("cli")
        for framework in ["react", "vue", "svelte", "next", "nuxt", "express", "fastify", "vite", "electron"]:
            if framework in all_deps:
                stack["frameworks"].append(framework)

    if pyproject or "requirements.txt" in names or "setup.py" in names:
        stack["languages"].append("Python")
        stack["package_managers"].append("pip")
        if "uv.lock" in names:
            stack["package_managers"].append("uv")
        if "poetry.lock" in names:
            stack["package_managers"].append("poetry")
        stack["project_types"].append("python")

    if "Cargo.toml" in names:
        stack["languages"].append("Rust")
        stack["package_managers"].append("cargo")
    if "go.mod" in names:
        stack["languages"].append("Go")
        stack["package_managers"].append("go")
    if any(path.endswith(".csproj") for path in paths):
        stack["languages"].append("C#")
        stack["package_managers"].append("dotnet")
    if "pom.xml" in names or "build.gradle" in names:
        stack["languages"].append("Java/Kotlin")

    if any("openai" in dep.lower() or "anthropic" in dep.lower() or "langchain" in dep.lower() for dep in all_deps):
        stack["project_types"].append("ai-app")
    if any(path.endswith(("openapi.yaml", "openapi.yml", "swagger.json")) for path in paths):
        stack["project_types"].append("api")

    for key in stack:
        stack[key] = sorted(set(stack[key]))
    return stack


def project_tree(root: Path, files: list[Path], limit: int = 120) -> list[str]:
    entries: list[str] = []
    for path in sorted(files, key=lambda item: rel(item, root)):
        relative = rel(path, root)
        if len(relative.split("/")) > 4:
            continue
        entries.append(relative)
        if len(entries) >= limit:
            break
    return entries


def analyze(root: Path) -> dict[str, Any]:
    root = root.resolve()
    files = iter_files(root)
    package = package_json_facts(root)
    pyproject = pyproject_facts(root)

    env_files = [
        path
        for path in files
        if path.name in {".env.example", ".env.sample", ".env.template"} or path.name.endswith(".env.example")
    ]
    committed_env_files = [
        rel(path, root)
        for path in files
        if path.name == ".env" or (path.name.startswith(".env.") and "example" not in path.name and "sample" not in path.name)
    ]

    assets = [
        {"path": rel(path, root), "kind": detect_asset_kind(path)}
        for path in files
        if path.suffix.lower() in ASSET_EXTENSIONS
    ]

    ci_files = [
        rel(path, root)
        for path in files
        if ".github/workflows/" in path.as_posix() or path.name in {".gitlab-ci.yml", ".travis.yml", "azure-pipelines.yml"}
    ]

    deployment_files = [
        rel(path, root)
        for path in files
        if path.name
        in {
            "Dockerfile",
            "docker-compose.yml",
            "compose.yml",
            "vercel.json",
            "netlify.toml",
            "fly.toml",
            "render.yaml",
            "Procfile",
        }
    ]

    docs = [rel(path, root) for path in files if path.name in DOC_FILES or path.parent.name.lower() == "docs"]

    env_vars: dict[str, list[str]] = {}
    for path in env_files:
        env_vars[rel(path, root)] = parse_env_file(path)

    make_targets = detect_make_targets(root / "Makefile")

    return {
        "project_root": str(root),
        "metadata": {
            "package_json": package,
            "pyproject": pyproject,
        },
        "stack": detect_stack(files, package, pyproject),
        "commands": {
            "package_scripts": (package or {}).get("scripts") or {},
            "python_scripts": (pyproject or {}).get("scripts") or {},
            "make_targets": make_targets,
        },
        "configuration": {
            "env_files": [rel(path, root) for path in env_files],
            "env_vars": env_vars,
            "committed_env_files": committed_env_files,
        },
        "documentation": {
            "docs": sorted(set(docs)),
            "ci_files": sorted(set(ci_files)),
            "deployment_files": sorted(set(deployment_files)),
            "license_files": sorted(rel(path, root) for path in files if path.name.upper().startswith("LICENSE")),
        },
        "assets": assets,
        "project_tree": project_tree(root, files),
        "warnings": [
            *(
                ["Committed .env-like files were found. Verify that no secrets are documented or exposed."]
                if committed_env_files
                else []
            ),
            *(["No README file found."] if not any(path.name.lower().startswith("readme") for path in files) else []),
            *(["No license file found."] if not any(path.name.upper().startswith("LICENSE") for path in files) else []),
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze README-relevant project facts.")
    parser.add_argument("project", nargs="?", default=".", help="Project directory to analyze.")
    parser.add_argument("--json", action="store_true", help="Print JSON output. This is the default format.")
    args = parser.parse_args()

    root = Path(args.project)
    if not root.exists() or not root.is_dir():
        parser.error(f"Project directory does not exist: {root}")

    print(json.dumps(analyze(root), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
