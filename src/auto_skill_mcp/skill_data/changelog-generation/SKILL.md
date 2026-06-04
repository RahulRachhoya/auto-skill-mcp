---
name: changelog-generation
description: Generate clear changelogs from commit history — grouped by type, linked to issues, written for humans.
metadata:
  category: general
  tags: [changelog, release, version, history]
---

# Changelog Generation

## Format (Keep a Changelog)
```markdown
# Changelog

## [1.1.0] - 2026-06-01

### Added
- New feature X (#42)
- Support for Y format

### Changed
- Improved performance of Z by 40%

### Fixed
- Bug where A crashed on empty input (#87)
- Memory leak in B

### Deprecated
- Legacy C endpoint (use D instead)

### Removed
- Deprecated E feature

### Security
- Fixed XSS vulnerability in search
```

## Rules
- Changelog is for humans, not machines
- Group by type: Added, Changed, Fixed, Removed, Deprecated, Security
- Reference issue/PR numbers
- Link to compare URLs between versions
- Credit contributors (optional but appreciated)
- Keep it up to date — write entries as you merge PRs, not at release time

## Generation
- `git log` with Conventional Commits → auto-generate
- Tools: `auto-changelog`, `standard-version`, `semantic-release`
- Manual review always — automated changelogs need editing
- Breaking changes get special attention and migration guides
