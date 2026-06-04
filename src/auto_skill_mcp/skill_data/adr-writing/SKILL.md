---
name: adr-writing
description: Write Architecture Decision Records — capture why decisions were made, what was considered, and the trade-offs.
metadata:
  category: documentation
  tags: [adr, architecture, decisions, documentation]
---

# ADR Writing

## When to Write an ADR
- Choosing between significant implementation approaches
- Adding a new framework, library, or external dependency
- Making a decision with long-term or cross-team impact
- Changing the project structure or architecture
- Deprecating or replacing an existing system
- Any decision you might need to explain to your future self

## Format
```markdown
# ADR-NNN: Title

## Status
[Proposed | Accepted | Deprecated | Superseded by ADR-NNN]

## Context
[The problem, constraints, and background information]

## Options Considered
[List 2-4 alternatives with pros and cons]

## Decision
[What was chosen and why]

## Consequences
[What becomes easier, harder, or different]

## Compliance
[How will the team verify this decision is followed?]
```

## Rules
- One ADR per decision (not per PR or per feature)
- Number sequentially (ADR-001, ADR-002)
- Store in `docs/adr/` directory
- Link superseded ADRs to their replacements
- Keep them short — one page is ideal
- Review and update stale ADRs quarterly
- ADRs are live documents — update when the decision changes
