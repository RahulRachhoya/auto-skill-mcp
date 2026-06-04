---
name: monitoring-setup
description: Set up observability with logs, metrics, and traces — know what your system is doing at all times.
metadata:
  category: devops
  tags: [monitoring, observability, metrics, logging, alerting]
---

# Monitoring Setup

## Three Pillars
1. **Logs** — structured, searchable records of events
2. **Metrics** — numerical measurements over time (latency, error rate, throughput)
3. **Traces** — end-to-end request flow across services

## What to Monitor
- **RED metrics**: Rate, Errors, Duration (for every service)
- **USE metrics**: Utilization, Saturation, Errors (for every resource)
- **Business metrics**: signups, orders, revenue — know if the business is working

## Alert Design
- Alert on symptoms (high error rate), not causes (high CPU)
- Set proper thresholds — too many alerts = ignored alerts
- Page for: user-facing errors, data loss, security incidents
- Email/Slack for: warnings, approaching thresholds
- Every alert must have a runbook link

## Logging Rules
- Structured format (JSON), not plain text
- Include: timestamp, level, service, trace_id, message
- No secrets in logs (PII, passwords, tokens)
- Log at the right level: DEBUG (dev), INFO (normal), WARN (concern), ERROR (broken)
