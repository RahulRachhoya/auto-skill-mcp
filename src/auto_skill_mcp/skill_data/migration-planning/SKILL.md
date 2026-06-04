---
name: migration-planning
description: Plan and execute data, schema, and service migrations safely — minimize risk and downtime.
metadata:
  category: devops
  tags: [migration, planning, data, schema, rollout]
---

# Migration Planning

## Principles
1. **Forward-only**: never modify a migration that has been applied
2. **Test on staging**: always run migrations on a copy of production data first
3. **Have a rollback**: every migration needs a tested rollback plan
4. **Make it reversible**: add column → deploy → remove column. Never done in one step

## Schema Migration
- Small, atomic changes per migration (one ALTER TABLE per file)
- Add columns as nullable first, backfill data, then add NOT NULL constraint
- Rename columns: add new column → dual-write → backfill → switch reads → drop old
- Run migrations during low-traffic periods
- Lock timeouts to prevent production impact

## Data Migration
- Back up before starting
- Run in batches with progress logging
- Verify row counts match after migration
- Test rollback on a copy of the data

## Service Migration (Strangler Fig)
1. Build new service alongside old
2. Route a small percentage of traffic to new service
3. Monitor for errors, latency, data consistency
4. Gradually increase traffic
5. Cut over completely when confident
6. Decommission old service
