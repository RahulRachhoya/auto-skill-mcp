---
name: pr-description
description: Write clear pull request descriptions that help reviewers understand what changed and why.
metadata:
  category: git
  tags: [pr, pull-request, review, description]
---

# PR Description

## Template
```markdown
## Summary
[1-3 bullet points of what this PR does]

## Changes
- `path/to/file.py`: [what changed and why]
- `path/to/other.py`: [what changed and why]

## Testing
- [x] Unit tests pass
- [x] Manual testing done
- [ ] Integration tests (if applicable)

## Related
Closes #123
```

## Rules
- **Small PRs are reviewed faster** — aim for <400 lines changed
- **One concern per PR** — don't mix refactoring with features
- **Link to issues** — "Closes #42" auto-closes on merge
- **Include screenshots** for UI changes (before/after)
- **Explain the why** — reviewers can read the diff for the what

## Checklist Before Opening
- [ ] All tests pass locally
- [ ] No debug code (console.log, print, breakpoints)
- [ ] No TODOs left in new code
- [ ] No secrets committed
- [ ] CHANGELOG updated (if applicable)
- [ ] Documentation updated (if applicable)
