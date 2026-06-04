---
name: code-review
description: Conduct systematic code reviews with clear quality gates, security checks, and actionable feedback.
metadata:
  category: code-quality
  tags: [review, quality, pr, feedback, pull-request]
---

# Code Review

## Overview
A systematic code review process with explicit gates: correctness, security, performance, maintainability, and style.

## Process
1. Understand context — read the PR description, linked issue, and affected files
2. Review for correctness first — does the code do what it claims?
3. Check security — OWASP Top 10, input validation, auth, data exposure
4. Evaluate performance — N+1 queries, unnecessary allocations, caching
5. Assess maintainability — naming, structure, test coverage, error handling
6. Write actionable feedback — specific lines, suggested code, reasoning

## Feedback Rules
- **Specific**: reference exact lines and symbols
- **Actionable**: "rename to `fetchUser`" not "this name is unclear"
- **Kind**: critique the code, not the author
- **Prioritized**: label severity (blocking, major, minor, nit)

## Gates
- [ ] All tests pass
- [ ] No new security concerns
- [ ] Error paths are handled
- [ ] Logging is appropriate (no secrets)
- [ ] New code has tests
- [ ] Public API is documented
- [ ] No dead code or commented-out blocks
