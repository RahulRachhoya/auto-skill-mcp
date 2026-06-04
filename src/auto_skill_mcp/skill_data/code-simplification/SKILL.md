---
name: code-simplification
description: Reduce code complexity while preserving behavior — fewer lines, clearer intent, less indirection.
metadata:
  category: code-quality
  tags: [simplify, complexity, maintainability, clarity]
---

# Code Simplification

## When to Simplify
- A function does more than one thing
- You need a comment to explain what the code does
- The same logic appears in multiple places
- There are more levels of indentation than 3
- You can't name the function without "and"

## Techniques
1. **Remove dead code** — anything not used. Version control has it
2. **Remove commented-out code** — that's what git history is for
3. **Merge duplicated branches** — if two if-branches do the same thing, merge them
4. **Flatten nesting** — early returns, guard clauses, invert conditions
5. **Replace loops with abstractions** — map/filter/reduce, list comprehensions
6. **Remove unnecessary wrappers** — functions that just call other functions
7. **Delete unnecessary abstractions** — if an interface has one implementation and is unlikely to get another, remove it

## Before/After

```python
# Before
def process(data):
    if data is not None:
        if len(data) > 0:
            result = []
            for item in data:
                if item.is_valid():
                    result.append(item.transform())
            return result
    return []
```

```python
# After
def process(data: list[Item] | None) -> list[Item]:
    if not data:
        return []
    return [item.transform() for item in data if item.is_valid()]
```

## Cost of Complexity
- Every abstraction has a cognitive cost
- Every indirection makes debugging harder
- Every unnecessary pattern is a reader tax
- Simple code is easier to test, review, and maintain
