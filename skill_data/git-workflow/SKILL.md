---
name: git-workflow
description: Use Git effectively — atomic commits, clean history, meaningful branching, and smooth collaboration.
metadata:
  category: git
  tags: [git, branching, commits, workflow, version-control]
---

# Git Workflow

## Branch Strategy
- `main` — production-ready, merges only from `develop` via PR
- `develop` — integration branch, feature branches merge here
- `feature/*` — one branch per task/feature
- `fix/*` — one branch per bug fix
- Never commit directly to `main` or `develop`

## Commit Rules
- **Atomic commits**: one logical change per commit. Don't mix refactoring with features
- **Conventional Commits**: `type(scope): description`
  - `feat`: new feature
  - `fix`: bug fix
  - `refactor`: code change without behavior change
  - `test`: adding/updating tests
  - `docs`: documentation
  - `chore`: config, deps, tooling
- Subject line: ≤50 chars, imperative mood ("add" not "added")
- Body: explain the why, not the what

## Git Commands
```bash
# Interactive rebase to clean up commits before PR
git rebase -i HEAD~N

# Fix up a commit (combine with parent, keep parent message)
git commit --fixup <sha> && git rebase -i --autosquash

# Bisect to find where a bug was introduced
git bisect start && git bisect bad && git bisect good <known-good>
```
