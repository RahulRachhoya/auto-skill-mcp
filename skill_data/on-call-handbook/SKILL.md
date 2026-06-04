---
name: on-call-handbook
description: Be effective on-call — prepare, triage, respond, and hand off with clear procedures.
metadata:
  category: general
  tags: [on-call, operations, incident, response]
---

# On-Call Handbook

## Before Your Shift
- Read recent incidents and postmortems
- Check the runbook is up to date for known issues
- Verify your access (production logs, dashboards, deployment tools)
- Know who to escalate to (your backup, senior engineers, manager)

## During Your Shift
- Respond to alerts within the SLO (usually 5-15 min for SEV-1)
- Acknowledge every alert — silence means no one is looking
- Triage first: who is affected? How badly? Is data at risk?
- Communicate: post in the incident channel with status updates
- Mitigate before fixing: stop the bleeding first

## Triage Flow
1. Is this real? (check monitoring, confirm with user reports)
2. What's the severity? (SEV-1/2/3/4)
3. Who needs to know? (team, manager, wider org)
4. What's the immediate fix? (rollback, feature flag, restart)
5. Document the timeline

## Handoff
- Write a clear handoff document: what's happening, what was tried, what's next
- Walk through the current state with the incoming on-call
- Don't hand off in the middle of an incident — stay until resolved or explicitly handed over
- Update the runbook with anything you learned
