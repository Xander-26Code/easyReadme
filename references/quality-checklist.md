# README Quality Checklist

Use this checklist before delivering a generated or improved README.

## Factual Accuracy

- [ ] `scripts/analyze_project.py` was run from the bundled skill directory when a local project was available, or manual scanning covered the same facts.
- [ ] Project name matches repository metadata or user notes.
- [ ] Description is supported by code, docs, or user notes.
- [ ] Feature list contains only verified features or clearly marked `TODO` items.
- [ ] Install commands come from real manifests, docs, or user notes.
- [ ] Run commands come from real manifests, docs, or user notes.
- [ ] Test commands come from real manifests, docs, or user notes.
- [ ] Build commands come from real manifests, docs, or user notes.
- [ ] Environment variables come from `.env.example`, docs, source code, or user notes.
- [ ] License is copied from the repository or marked `TODO`.
- [ ] No fake badges, demo links, screenshots, metrics, customers, or deployment URLs were added.
- [ ] Videos, images, avatars, star-history charts, sponsor links, and contributor blocks resolve to real files or verified external services.

## Developer Usefulness

- [ ] A new developer can understand the project purpose in under one minute.
- [ ] The setup path is visible near the top.
- [ ] Required prerequisites are listed.
- [ ] Configuration is explained.
- [ ] Usage examples match the real project type.
- [ ] Visual demos are included when they materially help users understand the project.
- [ ] Optional social-proof sections are useful for this project type, not decorative filler.
- [ ] Project structure highlights useful directories without dumping noise.
- [ ] Testing or verification steps are included when available.
- [ ] Known missing information is explicit.

## Structure And Polish

- [ ] `scripts/validate_readme.py` was run from the bundled skill directory for local README files, or any skipped validation is explained.
- [ ] Headings are consistent and scannable.
- [ ] Tables are used where they improve clarity.
- [ ] Code blocks include language tags.
- [ ] Links are relative when pointing to files in the repository.
- [ ] The tone is professional without generic marketing filler.
- [ ] The README avoids unnecessary sections that would be empty.
- [ ] Media assets have meaningful alt text or clear surrounding context.
- [ ] The file is valid Markdown.

## Final Response Checklist

When reporting back to the user, include:

- Files changed.
- Main sections added or improved.
- Important `TODO` items or missing facts.
- Optional media or social-proof assets the user may want to add.
- Script results from `analyze_project.py` or `validate_readme.py`, if run.
- Commands run, if any.
- Any verification that could not be completed.
