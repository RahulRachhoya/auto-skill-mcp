---
name: refactoring
description: Restructure code without changing behavior — improve readability, maintainability, and performance.
metadata:
  category: code-quality
  tags: [refactor, clean, restructure, maintainability]
---

# Refactoring

## Golden Rule
**Never refactor and add features at the same time.** Two separate changes, two separate commits/PRs.

## Process
1. **Ensure tests exist** before touching code. Add characterization tests if needed
2. **Identify the smell** — long function, duplicate code, god class, shotgun surgery, primitive obsession
3. **Apply one refactoring at a time** — extract, rename, move, inline
4. **Run tests after each step** — if tests break, revert the last change
5. **Commit frequently** — each atomic refactoring is one commit

## Common Refactorings
- **Extract Method** — turn a code block into a named function
- **Rename** — give variables, functions, and classes meaningful names
- **Replace Conditionals with Polymorphism** — if/else chains to strategy pattern
- **Introduce Parameter Object** — groups of related params into a single object
- **Decompose Conditional** — complex if/else into separate functions
- **Replace Magic Number with Constant**
- **Separate Query from Modifier**

## Signs You're Done
- Same behavior, same output
- Fewer lines of code
- Better names
- Clearer structure
- Tests still pass
