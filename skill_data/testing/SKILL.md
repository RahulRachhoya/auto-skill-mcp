---
name: testing
description: Write effective tests at the right level — unit, integration, and end-to-end — with meaningful coverage.
metadata:
  category: code-quality
  tags: [test, coverage, unit-test, integration-test, quality]
---

# Testing

## Test Pyramid
- **Unit tests** (70%) — test a single function/class in isolation. Fast, deterministic
- **Integration tests** (20%) — test components together (DB, API, filesystem). Slower but real
- **E2E tests** (10%) — test the full system. Slowest, most fragile, highest confidence

## Writing Good Tests
- **One assertion per logical concern** — not one giant assertion
- **Arrange-Act-Assert** — setup, execute, verify
- **Test behaviors, not implementation** — refactoring shouldn't break tests
- **Descriptive names** — `test_returns_empty_list_when_no_users_exist` not `test_users`
- **Use fixtures/mocks** for external dependencies, but prefer real instances when fast enough

## Coverage Guidelines
- Cover happy path, error path, and edge cases
- 80%+ line coverage is a good target
- 100% coverage is not the goal — meaningful coverage is
- Untested code is code you can't safely refactor

## What to Test
- Public API surfaces
- Boundary conditions (empty, null, max values)
- Error and failure paths
- Business logic (transformations, calculations, validations)
- Concurrency/race conditions where applicable
