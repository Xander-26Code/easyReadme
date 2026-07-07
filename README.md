# Easy README

Generate accurate, polished, GitHub-ready README files from real repository facts.

Easy README is a Claude Code skill for turning a project folder into a useful `README.md`. It combines a structured workflow, reusable README patterns, quality checks, and helper scripts so Claude can document projects without inventing features, commands, screenshots, licenses, or deployment details.

## Table Of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Bundled Scripts](#bundled-scripts)
- [Packaging And Distribution](#packaging-and-distribution)
- [Claude Code Notes](#claude-code-notes)
- [Other Compatible Agent Runtimes](#other-compatible-agent-runtimes)
- [Validation](#validation)
- [Optional Assets](#optional-assets)
- [License](#license)

## Overview

This repository is not a traditional application. It is a reusable Claude Code skill made of:

- `SKILL.md`: the main workflow and trigger instructions.
- `references/`: README templates, quality rules, and pattern examples.
- `scripts/`: deterministic helpers for project analysis and README validation.

The skill is designed for README creation, README improvement, GitHub documentation polishing, and enterprise-style project documentation. It works best when it can inspect a local repository and ground the generated README in actual files.

## Features

- Generates or improves project-specific `README.md` files.
- Extracts repository facts before drafting.
- Selects README shape by project type, such as CLI, library, AI app, backend API, full-stack product, or self-hosted app.
- Uses a pattern library distilled from strong open-source README structures.
- Marks missing facts as `TODO:` instead of inventing them.
- Suggests optional media and trust assets, such as screenshots, GIFs, videos, avatars, badges, sponsor links, or star-history charts, only when they are useful and verifiable.
- Validates generated READMEs for broken local links, missing recommended sections, unsupported package commands, media path issues, and TODO markers.

## Installation

This skill follows the open [Agent Skills](https://agentskills.io/) folder format and is optimized for Claude Code. It can also be used by other skills-compatible agent runtimes.

### Option 1: One Command With `npx skills`

Install from GitHub with the Skills CLI:

```bash
npx skills add Xander-26Code/easyReadme -a claude-code
```

For global installation across all Claude Code projects:

```bash
npx skills add Xander-26Code/easyReadme -a claude-code -g
```

During local development, install from this local folder:

```bash
npx skills add /Users/xander/easyReadme -a claude-code -g
```

Useful options:

| Option | Purpose |
|---|---|
| `-a claude-code` | Install specifically for Claude Code. |
| `-g` | Install globally under the user skills directory. |
| `--copy` | Copy files instead of symlinking. |
| `-y` | Skip confirmation prompts. |

Repository: https://github.com/Xander-26Code/easyReadme.git

### Option 2: Manual Install

Install globally for Claude Code:

```bash
mkdir -p ~/.claude/skills/easy-readme
cp -R /Users/xander/easyReadme/* ~/.claude/skills/easy-readme/
```

Or install only for one project:

```bash
mkdir -p .claude/skills/easy-readme
cp -R /Users/xander/easyReadme/* .claude/skills/easy-readme/
```

Manual install paths:

| Runtime | Install Path |
|---|---|
| Claude Code | `~/.claude/skills/easy-readme/` |
| Claude Code project | `.claude/skills/easy-readme/` |
| Cursor | `~/.cursor/skills/easy-readme/` |
| Codex CLI | `~/.codex/skills/easy-readme/` |
| Gemini CLI | `~/.gemini/skills/easy-readme/` |
| OpenCode | `~/.config/opencode/skills/easy-readme/` |

### Option 3: ZIP Upload To Claude

Claude custom skills can be uploaded as a ZIP file containing the skill folder.

```bash
mkdir -p /tmp/easy-readme-package
rsync -a --delete --exclude '.git' --exclude '__pycache__' --exclude '*.pyc' /Users/xander/easyReadme/ /tmp/easy-readme-package/easy-readme/
cd /tmp/easy-readme-package
zip -r /Users/xander/easy-readme-claude-skill.zip easy-readme
```

Upload:

```text
/Users/xander/easy-readme-claude-skill.zip
```

### Option 4: As Plain Reference Material

If a runtime does not support Agent Skills, paste `SKILL.md` into the conversation as instructions. The skill is still readable as plain Markdown with YAML frontmatter.

## Project Structure

```text
.
├── SKILL.md
├── README.md
├── references/
│   ├── pattern-library.md
│   ├── quality-checklist.md
│   └── readme-template.md
└── scripts/
    ├── analyze_project.py
    └── validate_readme.py
```

## How It Works

Easy README follows a five-phase workflow:

1. Clarify the README target, audience, tone, and output path.
2. Extract project facts from manifests, docs, scripts, CI files, deployment files, env examples, and media assets.
3. Choose a README shape from the base template or pattern library.
4. Draft the README with verified facts and explicit `TODO:` markers for missing information.
5. Validate the README and report what was verified, what changed, and what still needs user input.

## Quick Start

Use the skill directly in Claude Code by asking for a README task in a repository where the skill is installed:

```text
/easy-readme generate a polished README for this project
```

For project-local use, commit it under `.claude/skills/easy-readme/`:

```text
.claude/
└── skills/
    └── easy-readme/
        ├── SKILL.md
        ├── README.md
        ├── references/
        └── scripts/
```

## Usage

Ask Claude Code for the outcome you want and let the skill inspect the target repository:

```text
/easy-readme create a README for this repository
```

```text
/easy-readme improve the existing README and make it more polished, but do not invent missing deployment details
```

```text
/easy-readme audit this README and tell me what is missing before editing it
```

The skill will normally:

1. Run or simulate `${CLAUDE_SKILL_DIR}/scripts/analyze_project.py` to collect facts.
2. Read the relevant template or pattern reference.
3. Draft or update `README.md`.
4. Run or simulate `${CLAUDE_SKILL_DIR}/scripts/validate_readme.py`.
5. Report verified facts, warnings, and remaining missing information.

## Bundled Scripts

### Analyze A Project

Run this before drafting a README:

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/analyze_project.py" /path/to/project --json
```

The script reports:

- Project metadata.
- Detected stack and project type hints.
- Package scripts and Makefile targets.
- Environment example files and variables.
- CI, deployment, documentation, and license files.
- README-ready media assets.
- Basic warnings, such as missing license files.

### Validate A README

Run this after drafting or editing a README:

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/validate_readme.py" /path/to/project/README.md --project /path/to/project
```

The script checks:

- Local Markdown links.
- Local image, GIF, and video paths.
- Recommended sections.
- Common package-manager and Makefile commands.
- TODO markers.

## Packaging And Distribution

To prepare a Claude upload ZIP manually:

```bash
mkdir -p /tmp/easy-readme-package
rsync -a --delete --exclude '.git' --exclude '__pycache__' --exclude '*.pyc' /Users/xander/easyReadme/ /tmp/easy-readme-package/easy-readme/
cd /tmp/easy-readme-package
zip -r /Users/xander/easy-readme-claude-skill.zip easy-readme
```

The resulting archive contains one top-level `easy-readme/` folder with `SKILL.md`, `README.md`, `references/`, and `scripts/`.

For Team or Enterprise Claude workspaces, upload or share the skill through Claude's skill customization and organization sharing settings when enabled.

For cross-runtime publication, publish this repository to GitHub and use:

```bash
npx skills add Xander-26Code/easyReadme
```

## Claude Code Notes

- `SKILL.md` is the required entrypoint.
- The directory name controls the slash command. Use `easy-readme` if you want `/easy-readme`.
- `${CLAUDE_SKILL_DIR}` points to the installed skill directory and is the right way to reference bundled scripts.
- Project skills live under `.claude/skills/<skill-name>/`.
- Personal skills live under `~/.claude/skills/<skill-name>/`.
- Supporting files such as `references/` and `scripts/` are loaded or executed only when needed.

## Other Compatible Agent Runtimes

This skill uses the Agent Skills folder shape, so it may be portable to other compatible runtimes. The README and script paths are now optimized for Claude Code first.

## Validation

Current local validation:

```bash
python3 scripts/analyze_project.py . --json
python3 -m py_compile scripts/analyze_project.py scripts/validate_readme.py
```

The analyzer currently reports that this repository has no license file.

## Optional Assets

This project currently has no verified logo, screenshot, demo GIF, demo video, star-history chart, contributor image block, or sponsor asset. Those can be added later if the skill is published as an open-source project or shared Claude skill.

Good future assets would be:

- A short terminal GIF showing `analyze_project.py` and `validate_readme.py`.
- A before/after README example.
- A small logo or social preview image.
- A star-history chart after the project is public and has meaningful activity.

## License

MIT License
