---
name: easy-readme
description: Generate, improve, or rewrite README.md files for software projects with a polished, practical, enterprise-grade structure. Use this skill whenever the user asks to create a README, beautify a README, improve project documentation, make a GitHub README, write an enterprise README, structure a README, summarize a repository, document setup/usage/testing/deployment, or says Chinese phrases such as "生成 README", "美化 README", "写项目文档", "企业级 README", "让 README 更专业". This skill is especially important when the README must help a new developer clone, configure, run, understand, test, and deploy a project based on real repository facts rather than invented features.
---

# Easy README

Use this skill to create accurate, polished README files from a real project repository or user-provided project notes.

The goal is not just to write attractive Markdown. The goal is to turn messy project facts into a README that helps a developer, reviewer, recruiter, teammate, or open-source user quickly understand what the project is, how to run it, and what is still unknown.

## Core Principles

- Treat the README as the project's map for a new developer, not as a formality.
- Prefer repository facts over generic copywriting.
- Do not invent features, APIs, metrics, screenshots, deployment URLs, customers, licenses, badges, or roadmap items.
- If important information is missing, write `TODO:` or mention the gap in the final response.
- Match the README to the project type: frontend app, backend API, full-stack app, CLI, library, AI app, data project, mobile app, or documentation-only project.
- Prioritize a clear Quick Start path so a new developer can clone, install, configure, and run the project quickly.
- Treat media and social-proof assets as optional upgrades: useful when they clarify the project, noisy when they are decorative or unverifiable.
- Before large rewrites, pause long enough to understand the repository shape and the user's desired tone.
- Make the README useful first, beautiful second.

## When Starting

First determine the user's intent:

- **Create**: There is no README, or the user wants a new README from scratch.
- **Improve**: There is an existing README and the user wants it made clearer, prettier, more complete, or more professional.
- **Audit**: The user wants feedback on README quality without immediate rewriting.
- **Template**: The user wants a reusable README template rather than a project-specific README.

If the user's request is broad and files are available, inspect the project before writing. If the user explicitly asks to brainstorm or plan first, do not edit files until they confirm.

## Required Repository Scan

Use fast file discovery first, such as `rg --files`, then inspect the relevant files for the detected stack.

When this skill directory includes scripts and the user is working with a local repository, prefer running the bundled script from this skill directory. In Claude Code, use `${CLAUDE_SKILL_DIR}` so the script works from personal, project, or plugin skill locations.

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/analyze_project.py" /path/to/project --json
```

Use the JSON output as a factual inventory. If the script cannot run or the bundled script path is unavailable, continue with manual scanning.

Look for:

- Existing README files: `README.md`, `README.*`, docs landing pages.
- Project metadata: `package.json`, `pyproject.toml`, `setup.py`, `Cargo.toml`, `go.mod`, `pom.xml`, `build.gradle`, `.csproj`, `composer.json`, `Gemfile`, `pubspec.yaml`.
- Runtime and setup files: `.env.example`, `.env.sample`, `Dockerfile`, `docker-compose.yml`, `Makefile`, `Procfile`.
- Source entry points: app routes, CLI entry files, server files, package exports, main modules.
- Tests and quality tools: `tests/`, `__tests__/`, `spec/`, CI config, lint scripts.
- Deployment hints: `.github/workflows/`, `vercel.json`, `netlify.toml`, Kubernetes files, Terraform files.
- Project operations docs: `CHANGELOG.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, release config, version tags.
- Security and configuration hygiene: `.gitignore`, committed `.env` files, sample environment files, secret placeholders.
- Assets that can support documentation: screenshots, demo GIFs, videos, architecture diagrams, OpenAPI specs, logos, avatars, contributor images, star-history images, badges, and social preview assets.

Record facts mentally while scanning. Do not rely on filename guesses when a manifest or source file can confirm the fact.

## Reference Loading

Read only the references needed for the task:

- For README structure and section wording, read `references/readme-template.md`.
- When the user asks for a beautiful, high-star, GitHub-style, product-like, or template-driven README, read `references/pattern-library.md` before choosing the final shape.
- Before finalizing, read `references/quality-checklist.md`.

## Bundled Scripts

Use scripts as support tools, not as replacements for judgment.

- `scripts/analyze_project.py`: run before drafting when a local project is available. It extracts project metadata, commands, environment variables, docs, CI/deployment files, media assets, and warnings.
- `scripts/validate_readme.py`: run after creating or editing a README when the output is a local Markdown file. It checks local links, media paths, recommended sections, common package commands, and TODO markers.

When installed as a Claude Code skill, these script paths refer to the bundled files inside `${CLAUDE_SKILL_DIR}`, not files inside the user's target project.

If a script reports warnings, use them to improve the README or mention them in the final response. If a script reports false positives, explain why they are safe to ignore.

## Workflow

### Phase 0: Clarify the Target

Identify:

- Audience: open-source users, internal team, recruiter, enterprise buyer, API consumer, course evaluator, or personal portfolio viewer.
- Tone: concise professional, product-like, developer-focused, enterprise, academic, or friendly open-source.
- Output location: usually `README.md` in the project root unless the user asks for a draft elsewhere.

If the user gives no preference, use a concise professional tone with practical developer details.

### Phase 1: Extract Project Facts

Create a factual inventory from repository files:

- Run `scripts/analyze_project.py` through `${CLAUDE_SKILL_DIR}` when available, then inspect important files manually to confirm the output.

- Project name.
- One-sentence purpose.
- Tech stack.
- Key features that are visible in code, config, docs, or user notes.
- Installation requirements.
- Prerequisites.
- Environment variables.
- Clone, install, configure, and development run steps.
- Run commands.
- Test commands.
- Build commands.
- CI workflow, if present.
- Deployment commands or hosting platform, if known.
- Project structure.
- Architecture overview, if it can be inferred from code or docs.
- API endpoints, CLI commands, or package API, when visible in code or docs.
- Changelog or versioning approach, if present.
- Contribution and code of conduct files, if present.
- Available media assets: screenshots, GIFs, videos, logos, avatars, architecture diagrams, demo recordings, or social images.
- Existing social proof: stars, downloads, package stats, contributors, sponsors, star-history charts, or community links, only when backed by real services or repository data.
- License, if present.

Mark uncertain items as unknown. Do not smooth over uncertainty.

### Phase 2: Choose README Shape

Use the detected project type to choose sections from `references/readme-template.md`.

Common sections:

- Title and concise value proposition.
- Hero media or centered masthead, when the project has suitable assets.
- Overview.
- Demo video, GIF, screenshot gallery, or live demo link, when available.
- Features.
- Tech stack.
- Quick Start.
- Prerequisites.
- Installation.
- Environment variables.
- Development.
- Project structure.
- Architecture overview, when useful.
- Usage.
- Scripts or commands.
- API reference, CLI reference, or package usage, when relevant.
- Testing.
- Continuous Integration, when configured.
- Deployment.
- Versioning and changelog, when present or important.
- Roadmap.
- Contributing.
- Code of conduct, when present or appropriate.
- Contributors, author, sponsor/support, star history, or community links, when they are relevant and verified.
- License.

Omit sections that would be empty or misleading. Use `TODO:` for important missing facts the user should fill in.

Use a table of contents for long READMEs, especially when the README includes setup, architecture, API, testing, CI, deployment, and contribution sections.

### Phase 3: Draft Carefully

When creating or rewriting `README.md`:

- Keep headings scannable.
- Put the most important setup path near the top.
- Ask or infer whether optional visual/social assets should be included when the project would benefit from them: demo video, screenshot, GIF, logo, author avatar, contributor avatars, sponsor block, star-history chart, download badges, package badges, or community badges.
- If the asset exists, embed it with stable relative paths or verified external URLs. If it would help but is missing, add a short `TODO:` suggestion instead of inventing it.
- Make Quick Start a practical path: clone the repo, install dependencies, copy or create environment files, run backend/frontend/services, and open the local URL if verified.
- Use tables for commands, environment variables, and API endpoints when they improve readability.
- Use fenced code blocks with language tags.
- Include example API requests/responses, screenshots, or demo GIFs only when they exist in the repo, are provided by the user, or can be derived from verified docs/tests.
- Explain repository structure with short descriptions for important folders rather than dumping every file.
- Document CI only when workflows or scripts exist. If CI is missing but relevant, mark it as `TODO:` instead of pretending it exists.
- Mention versioning or changelog only when the repo contains related files/tags or the user requests a professional template.
- Warn about configuration and secret handling when `.env` files or API keys are part of setup.
- Use relative links for repository files when possible.
- Keep claims proportional to evidence.
- Avoid over-decorating with badges unless the repo already has the underlying services configured.

For existing READMEs, preserve valuable project-specific content. Improve structure and clarity without deleting useful details merely because they do not fit the template.

### Phase 4: Verify

Before finalizing, run the quality checklist in `references/quality-checklist.md`.

If a README file exists locally after drafting, run:

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/validate_readme.py" /path/to/project/README.md --project /path/to/project
```

Use the validation output to catch broken links, missing recommended sections, unverified package commands, and media path issues.

Check especially:

- Are install, run, build, and test commands copied from real manifests or docs?
- Can a new developer follow the Quick Start without guessing the missing middle steps?
- Is the intended "clone to running locally" path likely achievable in about 10 minutes for a prepared developer?
- Did the README invent a feature, endpoint, deployment URL, metric, or license?
- Are environment variables documented without exposing secrets?
- Does the repository structure explain what important folders do?
- Are screenshots, example requests, or response examples included when they are available and useful?
- Are optional videos, screenshots, avatars, badges, star-history charts, sponsor links, or contributor blocks included only when they add real trust or clarity?
- Do all media links resolve to real files or verified external services?
- Is CI documented only if it exists, or clearly marked as a future improvement?
- Is versioning/changelog guidance included when the project has release history or asks to look production-ready?
- Are missing values clearly marked?
- Would a new developer know what to do next?
- Does the README look polished without sounding like generic marketing?

### Phase 5: Report

After editing or drafting, tell the user:

- Which files changed.
- Which facts were verified from the repository.
- Whether `analyze_project.py` or `validate_readme.py` was run, and the key result.
- Which important items remain `TODO` or uncertain.
- Any commands you ran for verification.

Keep the final response concise. Do not paste the entire README unless the user asks for it.

## Accuracy Rules

Use only facts found in:

- Repository files.
- Existing documentation.
- User-provided notes.
- Directly inspected source code.
- Current command output.

Do not fabricate:

- Feature lists.
- API endpoints.
- Screenshots.
- Demo URLs.
- Media assets.
- Star-history charts.
- Production deployments.
- Performance numbers.
- Test coverage.
- License.
- Company/customer adoption.
- Compatibility promises.

If information is plausible but unverified, either omit it or write `TODO:`.

## Output Defaults

For a project-specific request, write or update `README.md` in the repository root.

For a draft-only request, write to `README.generated.md` unless the user specifies another path.

For an audit-only request, do not edit files. Return findings ordered by importance, with concrete suggestions.
