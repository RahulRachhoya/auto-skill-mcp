---
name: technical-debt-management
description: Track, prioritize, and pay down technical debt systematically without breaking product delivery.
metadata:
  category: code-quality
  tags: [debt, technical-debt, quality, maintenance]
---

# Technical Debt Management

## Debt Types
- **Reckless vs Prudent**: Did you know it was debt? Was it intentional?
- **Code debt**: complexity, duplication, dead code
- **Design debt**: wrong abstractions, over-engineering
- **Test debt**: missing coverage, flaky tests
- **Documentation debt**: missing or outdated docs

## Management Process
1. **Inventory** — keep a living list of known debt items with context
2. **Quantify impact** — how much time does this cost per week? How much risk?
3. **Prioritize** — fix debt in code you touch (scout rule: leave it cleaner than you found it)
4. **Budget time** — allocate 20% of each sprint to debt reduction
5. **Track progress** — measure metrics like test coverage, cyclomatic complexity, build time

## When to Fix vs Defer
| Fix Now | Defer | Accept |
|---------|-------|--------|
| Blocks development | Cosmetic issues | Known, documented risks |
| Causes production bugs | Out-of-style patterns | One-time migration costs |
| Creates security risk | Well-understood limitations | Strategic shortcuts |
| Increases all future changes | Low-impact violations | Deprecated code scheduled for removal |
