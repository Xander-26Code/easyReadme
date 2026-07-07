# README Template Reference

Use this reference to shape project-specific READMEs. Do not include every section automatically. Select the sections that match the repository and the user's goal.

When available, use `scripts/analyze_project.py` output to fill this template with verified facts. In Claude Code, run bundled scripts through `${CLAUDE_SKILL_DIR}`. After drafting a local README, use `scripts/validate_readme.py` to catch broken local links, media path issues, and unsupported command claims.

## Standard Project README

```markdown
# Project Name

Short, concrete one-sentence description of what the project does and who it is for.

<!-- Optional: add a verified logo, screenshot, GIF, demo video thumbnail, or star-history image when it improves trust or clarity. -->

## Overview

Explain the problem, the solution, and the primary user or developer workflow in 1-3 short paragraphs.

## Demo

Add one of these only when available and useful:

- Screenshot: `![Screenshot](path-or-url)`
- GIF demo: `![Demo](path-or-url)`
- Video link: `[Watch demo](url)`
- Live demo: `[Open live demo](url)`
- Star history or growth chart from a verified service.

## Features

- Verified feature from code, docs, or user notes.
- Verified feature from code, docs, or user notes.
- `TODO:` Missing feature detail that needs confirmation.

## Tech Stack

| Area | Technology |
|---|---|
| Frontend | TODO |
| Backend | TODO |
| Database | TODO |
| Testing | TODO |
| Deployment | TODO |

## Project Structure

```text
.
├── src/
├── tests/
└── README.md
```

## Getting Started

### Prerequisites

- Runtime or tool version, if verified.
- Package manager, if verified.

### Installation

```bash
command copied from real project files
```

### Configuration

| Variable | Required | Description |
|---|---:|---|
| `TODO` | Yes | TODO |

### Development

```bash
command copied from real project files
```

## Usage

Show the shortest real usage path. For apps, this may be a local URL. For CLIs, show commands. For libraries, show import examples that match the exported API.

## Scripts

| Command | Description |
|---|---|
| `TODO` | TODO |

## Testing

```bash
command copied from real project files
```

## Build

```bash
command copied from real project files
```

## Deployment

Document only verified deployment steps or hosting configuration. Otherwise write `TODO: Add deployment instructions`.

## Roadmap

- `TODO:` Confirm planned improvements.

## Community And Social Proof

Use this section only when relevant and verified:

- Author or maintainer profile.
- Contributor avatars or contributor graph.
- Sponsor/support links.
- Star-history chart.
- Package downloads or usage badges.
- Discord, Slack, forum, or community links.

## Contributing

Add practical contribution steps if the project is open to contributions.

## License

Use the license found in the repository. If no license exists, write `TODO: Add license`.
```

## Frontend App Sections

Prefer these additions when the project is primarily a UI:

- Screenshots or demo GIFs, only if assets exist or the user provides them.
- Demo videos or live demo links, only when verified.
- User flows.
- Component or page structure.
- Design system notes, if present.
- Browser support, only if configured or documented.

## Backend API Sections

Prefer these additions when the project exposes an API:

- API overview.
- Authentication model, if verified.
- Endpoint table from routes or OpenAPI files.
- Request and response examples from tests, docs, or code.
- Database or migration setup.
- Observability or logging notes, if verified.

## CLI Sections

Prefer these additions when the project is a command-line tool:

- Installation method.
- Command synopsis.
- Options table.
- Examples.
- Exit codes, only if documented or visible in code.

## Library Sections

Prefer these additions when the project is a reusable package:

- Installation command.
- Minimal import example.
- Public API surface.
- Version compatibility.
- Publishing instructions only if relevant and verified.

## AI App Sections

Prefer these additions when the project uses AI models or agents:

- Model/provider configuration.
- Required API keys.
- Data privacy notes, if documented.
- Prompt or tool architecture, if visible.
- Evaluation or testing approach, if present.

## Style Notes

- Lead with concrete value, not generic adjectives.
- Keep paragraphs short.
- Prefer "what it does" over "what it aspires to be".
- Use `TODO:` for missing but important information.
- Avoid badges unless their backing service exists.
- Suggest optional media or social-proof assets when they would improve the README, but do not add fake or decorative assets.
