---
name: debugging
description: Systematic approach to finding and fixing bugs — reproduce, isolate, fix, and prevent regression.
metadata:
  category: code-quality
  tags: [debug, bug, error, fix, troubleshooting]
---

# Debugging

## Process
1. **Reproduce** — get a reliable reproduction case with minimal steps
2. **Read the error** — stack traces tell you exactly where and what. Parse them fully before touching code
3. **Form a hypothesis** — what could cause this? List 2-3 possibilities
4. **Isolate** — binary search: comment out half the code, check if error persists. Use `git bisect` for regressions
5. **Fix** — smallest change that resolves the root cause
6. **Guard** — add a test that would catch this bug, add logging for next time

## Techniques
- **Rubber duck**: explain the problem aloud. The fix often appears mid-explanation
- **Divide and conquer**: binary search through commits (`git bisect`), files, or functions
- **Minimal repro**: strip away everything non-essential until only the bug remains
- **Read the docs**: especially for library/framework behavior you assume you understand
- **Check the data**: many bugs are not logic errors but unexpected input

## Common Root Causes
- Null/undefined values where you expected a value
- Off-by-one in loops or indexing
- Race conditions from shared mutable state
- Incorrect assumption about API behavior
- Environment differences (dev vs prod configs)
