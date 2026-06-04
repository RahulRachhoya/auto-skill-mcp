---
name: incident-response
description: Respond to production incidents systematically — triage, mitigate, resolve, and learn.
metadata:
  category: devops
  tags: [incident, response, on-call, production, outage]
---

# Incident Response

## Process
1. **Triage** — assess severity and impact. Is anyone affected? Is data at risk?
2. **Mitigate** — stop the bleeding (rollback, feature flag off, block traffic). Fix comes after
3. **Communicate** — post in the incident channel: what happened, impact, who's working, ETA
4. **Resolve** — apply the permanent fix
5. **Follow-up** — postmortem within 48 hours

## Severity Levels
| Level | Response | Example |
|-------|----------|---------|
| SEV-1 | Page team, escalate | Complete outage, data loss |
| SEV-2 | Page on-call | Feature broken for many users |
| SEV-3 | Working hours | Minor bug, cosmetic issue |
| SEV-4 | Track in backlog | Low-impact, no users affected |

## Postmortem Template
```
## Summary
[One paragraph of what happened]

## Timeline
- [Time] User reports issue
- [Time] On-call paged
- [Time] Mitigation applied (rollback)
- [Time] Service healthy

## Root Cause
[What actually caused the incident]

## Action Items
- [ ] Short-term fix: ...
- [ ] Long-term prevention: ...

## Lessons Learned
[What the team learned. Blameless.]
```

## Rules
- **Blameless postmortems** — systems fail, not people
- **Fix the process, not the person** — how did the system allow this?
- **Every incident is a learning opportunity** — improve runbooks, add alerts, automate prevention
