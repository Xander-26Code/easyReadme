# README Pattern Library

This file distills reusable README patterns from strong open-source examples. Use these patterns as structural inspiration, not as copywriting to imitate.

Do not copy project-specific wording, badges, images, logos, claims, examples, contributor sections, or brand voice. Extract the information architecture: what appears first, how the reader is guided, what proof is shown, and how setup is made easy.

## How To Choose A Pattern

Choose by project type and user intent:

| User Need | Best Pattern |
|---|---|
| Desktop app, visual app, polished portfolio project | Visual Product App |
| CLI tool with fast install and usage | CLI Tool |
| Library or framework with code-first onboarding | Framework Or Library |
| Full-stack SaaS or product platform | Product Platform |
| AI app or agent product | AI Product |
| Backend/API/documentation tool | API Or Docs Tool |
| Developer tool with changelog/release workflow | DevOps Utility |
| Chat/community app or self-hosted app | Self-Hosted Web App |
| Enterprise/data workflow tool | Data Platform |
| README generator or meta-tool | Meta Documentation Tool |

## The 10 Reference Examples

These are the selected examples and the reusable lesson from each one.

| Example | Type | Reusable Pattern |
|---|---|---|
| `amitmerchant1990/electron-markdownify` | Desktop app | Centered visual hero, badges, quick nav, GIF demo, features, install, download, credits, related projects. |
| `kefranabg/readme-md-generator` | Meta documentation CLI | Badges, concise pitch, demo first, usage commands, template customization, contributors, support, license. |
| `httpie/httpie` | CLI/API client | Brand-forward intro, getting started, features, examples, community, contribution path. |
| `gofiber/fiber` | Web framework | Quickstart early, benchmarks, feature inventory, philosophy, limitations, examples, middleware ecosystem, development. |
| `dbt-labs/dbt-core` | Data platform | Clear product explanation for newcomers, supported environments, conceptual overview, getting started, community, bug/contribution links. |
| `PostHog/posthog` | Product platform | Product-positioning intro, table of contents, cloud vs self-hosting paths, setup, learning links, contributing, paid/open-source boundary. |
| `lobehub/lobe-chat` | AI product | Modern hero, community callouts, feature narrative, self-hosting options, environment variables, ecosystem/plugins, local development, sponsors. |
| `github-changelog-generator/github-changelog-generator` | DevOps utility | Problem framing, installation, usage modes, output example, parameters, migration guide, features, alternatives, FAQ. |
| `gui-cs/Terminal.Gui` | UI library | Concise capability statement, quick start, minimal runnable example, showcase, docs links, installation, contribution, history. |
| `thelounge/thelounge` | Self-hosted web app | Centered hero, overview, installation paths for releases/source, development setup. |

Sources:

- https://github.com/matiassingers/awesome-readme
- https://github.com/amitmerchant1990/electron-markdownify
- https://github.com/kefranabg/readme-md-generator
- https://github.com/httpie/httpie
- https://github.com/gofiber/fiber
- https://github.com/dbt-labs/dbt-core
- https://github.com/PostHog/posthog
- https://github.com/lobehub/lobe-chat
- https://github.com/github-changelog-generator/github-changelog-generator
- https://github.com/gui-cs/Terminal.Gui
- https://github.com/thelounge/thelounge

## Pattern 1: Visual Product App

Best for desktop apps, mobile apps, portfolio apps, editor tools, and UI-heavy projects.

Use when the project has screenshots, a GIF, downloads, or clear user-facing features.

````markdown
<h1 align="center">
  <br>
  <img src="path-or-url" alt="Project Name" width="160">
  <br>
  Project Name
  <br>
</h1>

<h4 align="center">One sentence explaining what the app is and who it helps.</h4>

<p align="center">
  <!-- verified badges only -->
</p>

<p align="center">
  <a href="#features">Features</a> |
  <a href="#quick-start">Quick Start</a> |
  <a href="#download">Download</a> |
  <a href="#credits">Credits</a> |
  <a href="#license">License</a>
</p>

![Demo](path-or-url)

## Features

- Verified feature.
- Verified feature.
- Verified feature.

## Quick Start

```bash
git clone TODO
cd TODO
TODO
```

## Download

TODO: Add release links or installation packages.

## Credits

TODO: Add third-party libraries or acknowledgements.

## Related

TODO: Add related projects only if verified.

## License

TODO
````

Design notes:

- Put visual proof above the fold.
- Use badges only if they point to real services.
- Keep the intro short because the screenshot/GIF carries the story.

## Pattern 2: CLI Tool

Best for command-line tools, developer utilities, generators, and automation scripts.

````markdown
# Project Name

One sentence explaining the command and the job it performs.

![Demo](path-or-url)

## Installation

```bash
TODO
```

## Quick Start

```bash
TODO
```

## Usage

```bash
project-command [options]
```

| Option | Description |
|---|---|
| `TODO` | TODO |

## Examples

```bash
TODO
```

## Configuration

TODO: Document config files, environment variables, or defaults.

## FAQ

TODO

## Contributing

TODO

## License

TODO
````

Design notes:

- Lead with copy-paste commands.
- Show output examples when available.
- Prefer examples over long prose.

## Pattern 3: Framework Or Library

Best for packages, SDKs, frameworks, UI libraries, and reusable modules.

````markdown
# Project Name

Short capability statement for developers.

## Quick Start

```bash
TODO
```

## Minimal Example

```language
TODO
```

## Features

- Verified capability.
- Verified capability.

## Installation

```bash
TODO
```

## Documentation

- [Getting Started](TODO)
- [API Reference](TODO)
- [Examples](TODO)

## Examples

TODO: Link or include common examples.

## Limitations

TODO: Add known limitations if documented.

## Development

```bash
TODO
```

## Contributing

TODO

## License

TODO
````

Design notes:

- Put the smallest runnable example near the top.
- Document limitations honestly when they shape adoption decisions.
- Link out to full docs instead of making README unreadably long.

## Pattern 4: Product Platform

Best for full-stack SaaS, analytics platforms, product suites, and internal platforms.

````markdown
# Project Name

Clear product positioning sentence.

## Table of Contents

- [Getting Started](#getting-started)
- [Setup](#setup)
- [Architecture](#architecture)
- [Learning More](#learning-more)
- [Contributing](#contributing)

## Getting Started

### Hosted Option

TODO: Add cloud or managed option only if verified.

### Self-Hosted Option

TODO: Add self-hosting path only if verified.

## Setup

```bash
TODO
```

## Configuration

| Variable | Required | Description |
|---|---:|---|
| `TODO` | Yes | TODO |

## Architecture

TODO: Explain major services, apps, packages, queues, databases, and integrations.

## Learning More

- Documentation: TODO
- Community: TODO
- Issues: TODO

## Open Source And Commercial Features

TODO: Clarify boundaries if relevant.

## Contributing

TODO

## License

TODO
````

Design notes:

- Separate hosted and self-hosted paths.
- Make product boundaries explicit.
- Add architecture only when it helps contributors run or modify the project.

## Pattern 5: AI Product

Best for AI chat apps, agent platforms, model-powered tools, and prompt-heavy apps.

````markdown
# Project Name

One sentence explaining the AI workflow and target user.

## Getting Started

```bash
TODO
```

## Features

- Verified AI feature.
- Verified collaboration or automation feature.
- Verified deployment feature.

## Model And Provider Setup

| Provider | Required Variables | Notes |
|---|---|---|
| TODO | TODO | TODO |

## Self Hosting

### Option A: Managed Deployment

TODO

### Option B: Docker

TODO

## Environment Variables

| Variable | Required | Description |
|---|---:|---|
| `TODO` | Yes | TODO |

## Local Development

```bash
TODO
```

## Plugins Or Integrations

TODO

## Privacy And Data Notes

TODO: Add only verified behavior around data storage, model calls, and logging.

## Contributing

TODO

## License

TODO
````

Design notes:

- Make provider/API-key setup unmistakable.
- Do not invent privacy guarantees.
- Separate local development from deployment.

## Pattern 6: API Or Docs Tool

Best for API renderers, developer portals, SDK documentation tools, and backend API products.

````markdown
# Project Name

One sentence explaining what documentation or API workflow it improves.

## Live Demo

TODO: Add verified demo link.

## TL;DR

```bash
TODO
```

## Features

- Verified feature.
- Verified feature.

## Installation

```bash
TODO
```

## Usage

```bash
TODO
```

## Example Input

```language
TODO
```

## Example Output

```language
TODO
```

## Configuration

TODO

## API Reference

TODO: Link to complete docs or summarize verified endpoints/options.

## License

TODO
````

Design notes:

- Show before/after or input/output when possible.
- Keep examples accurate and runnable.
- Link to full API docs rather than bloating the README.

## Pattern 7: DevOps Utility

Best for release tools, CI helpers, changelog generators, backup tools, and workflow automation.

````markdown
# Project Name

One sentence explaining what repetitive operational task this automates.

## Why This Exists

Explain the problem in a few short paragraphs.

## Installation

```bash
TODO
```

## Usage

### CLI

```bash
TODO
```

### Docker

```bash
TODO
```

## Output Example

```text
TODO
```

## Configuration And Parameters

| Parameter | Description | Default |
|---|---|---|
| `TODO` | TODO | TODO |

## Migration Guide

TODO: Add when replacing manual or legacy workflow.

## Alternatives

TODO: List alternatives only if useful and fair.

## FAQ

TODO

## Contributing

TODO

## License

TODO
````

Design notes:

- Start with pain and workflow clarity.
- Include output examples because users want to know what the tool produces.
- Add alternatives when the ecosystem is crowded.

## Pattern 8: Self-Hosted Web App

Best for self-hosted apps, community tools, chat apps, dashboards, and deployable web services.

````markdown
# Project Name

Short app description and primary use case.

![Screenshot](path-or-url)

## Overview

Explain what the app does and who runs it.

## Installation And Usage

### Stable Release

```bash
TODO
```

### From Source

```bash
TODO
```

## Configuration

| Variable / File | Description |
|---|---|
| `TODO` | TODO |

## Development Setup

```bash
TODO
```

## Deployment

TODO

## Contributing

TODO

## License

TODO
````

Design notes:

- Separate user install from contributor setup.
- Include screenshots because self-hosted users need to know what they are running.
- Be clear about stable release vs source build.

## Pattern 9: Data Platform

Best for analytics, data transformation, ML/data workflow tools, and data infrastructure projects.

````markdown
# Project Name

One sentence explaining the data workflow the project supports.

## Understanding The Project

Explain the concepts a new user must know before setup.

## Supported Environments

| OS / Runtime | Status |
|---|---|
| TODO | TODO |

## Getting Started

```bash
TODO
```

## Core Workflow

1. TODO
2. TODO
3. TODO

## Project Structure

```text
TODO
```

## Documentation

- Getting started: TODO
- Concepts: TODO
- Reference: TODO

## Community And Support

TODO

## Reporting Bugs And Contributing

TODO

## License

TODO
````

Design notes:

- Explain concepts before commands if the domain is unfamiliar.
- Make supported environments visible.
- Point users to deeper docs early.

## Pattern 10: Meta Documentation Tool

Best for README generators, docs generators, template engines, and documentation automation.

````markdown
# Project Name

Short sentence explaining what documentation artifact it generates.

## Demo

Show the tool in action with a GIF, screenshot, or terminal recording.

## Generated Output

Show or link to the generated artifact.

## Usage

```bash
TODO
```

## Options

| Option | Description |
|---|---|
| `TODO` | TODO |

## Templates

Explain how users can provide custom templates.

## Metadata Sources

Document what files the tool reads, such as package metadata, git config, project manifests, or user prompts.

## Contributing

TODO

## Support

TODO

## License

TODO
````

Design notes:

- Show generated output, not just the generator.
- Explain defaults and customization.
- Document what project facts are automatically detected.

## Cross-Pattern Rules

- Use a visual hero only when there is a real logo, screenshot, GIF, or demo.
- Prompt the user about optional media and trust assets when appropriate: demo video, screenshots, GIFs, author avatar, contributor avatars, sponsor links, star-history chart, download badges, package badges, or community badges.
- Add a table of contents when the README is long enough to require navigation.
- Badges should prove useful facts: package version, build, coverage, docs, license, downloads, security, or community.
- Star-history charts and contributor blocks belong in open-source or community-driven projects; skip them for small private/internal projects unless the user asks.
- Put Quick Start before deep architecture unless the project cannot be understood without domain concepts.
- Include screenshots/GIFs for visual apps, terminal demos for CLIs, code snippets for libraries, and input/output examples for generators.
- Keep contribution, sponsor, credits, and community sections near the end unless community is the product's main value.
- Every template section is optional. Delete empty sections rather than shipping placeholders, except for important missing facts that should remain as `TODO:`.
