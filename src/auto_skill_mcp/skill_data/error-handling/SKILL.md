---
name: error-handling
description: Handle errors predictably and gracefully — never lose errors, never hide them, never crash unexpectedly.
metadata:
  category: code-quality
  tags: [error, exception, handling, robustness]
---

# Error Handling

## Principles
1. **Never swallow errors** — empty catch blocks are bugs
2. **Never expose internals in error messages** — no stack traces to users
3. **Fail fast** — validate inputs early, crash on invalid state
4. **Handle errors at the right level** — don't catch what you can't handle

## Patterns
- **Return typed results** — Result/Option types instead of exceptions for expected failures
- **Use exceptions for exceptional cases** — not for control flow
- **Wrap external errors** — translate third-party errors into your domain
- **Add context** — include what you were doing when the error occurred
- **Graceful degradation** — if a non-critical feature fails, the app should still work

## Checklist
- [ ] Every public function documents what errors it can produce
- [ ] Every catch block either handles, wraps with context, or re-raises
- [ ] External API calls have timeout and retry logic
- [ ] User-facing errors don't leak implementation details
- [ ] Errors are logged with enough context to debug
- [ ] Null/None checks are explicit, not implicit
