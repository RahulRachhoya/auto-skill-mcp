---
name: commit-messages
description: Write clear, structured commit messages that explain why, not just what.
metadata:
  category: git
  tags: [commit, messages, git, conventional-commits]
---

# Commit Messages

## Structure
```
type(scope): description

Body — explain why this change exists, not what it does.
```

## Types
| Type | When |
|------|------|
| `feat` | New feature |
| `fix` | Bug fix |
| `refactor` | Code change with no behavior change |
| `test` | Adding/updating tests |
| `docs` | Documentation |
| `chore` | Config, deps, CI, tooling |
| `perf` | Performance improvement |
| `style` | Formatting (no code change) |

## Rules
- **Subject**: ≤50 chars, imperative ("add" not "added" or "adds")
- **Body**: wrap at 72 chars, explain motivation
- **Scope**: optional but helpful: `feat(api):` or `fix(auth):`
- **Breaking changes**: add `!` after type: `feat(api)!: remove deprecated v1 endpoint`
- **Reference issues**: `fix #123` in the body

## Examples
```
feat(auth): add password reset flow

Users can now request a password reset email. Token expires in 15 minutes.

Closes #42
```

```
fix(db): handle null created_at on legacy records

Some records created before migration v3 have null timestamps.
Default to current timestamp instead of crashing.

Fixes #87
```
