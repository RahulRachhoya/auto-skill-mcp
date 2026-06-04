---
name: architecture-decisions
description: Document architecture decisions as ADRs — capture context, options, decision, and consequences.
metadata:
  category: architecture
  tags: [architecture, adr, decisions, documentation]
---

# Architecture Decisions

## ADR Format
```
# ADR-NNN: Title

## Status
[Proposed | Accepted | Deprecated | Superseded]

## Context
What is the problem? What constraints exist? What is the background?

## Options Considered
Option A: Description
  - Pros: ...
  - Cons: ...
Option B: Description
  - Pros: ...
  - Cons: ...

## Decision
Chosen option and rationale.

## Consequences
What becomes easier? What becomes harder? What trade-offs were accepted?

## Compliance
How will we verify this decision is followed?
```

## When to Write an ADR
- Adding a new dependency or framework
- Choosing between significant implementation approaches
- Changing the project structure
- Making a decision with long-term impact
- Deprecating or replacing an existing system

## Rules
- Keep them short — one page is ideal
- Date every ADR
- Link related ADRs
- Superseded ADRs reference the replacement
- Store in `docs/adr/` as numbered files
