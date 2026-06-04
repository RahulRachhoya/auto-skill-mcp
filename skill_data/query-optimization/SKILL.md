---
name: query-optimization
description: Optimize database queries — indexes, EXPLAIN plans, N+1 prevention, and connection management.
metadata:
  category: general
  tags: [query, database, sql, optimization, performance]
---

# Query Optimization

## Process
1. **Identify slow queries** — database logs, slow query log, APM tools
2. **EXPLAIN ANALYZE** — understand the query plan. Look for seq scans, large sorts
3. **Index missing?** — add indexes for WHERE, JOIN, ORDER BY columns
4. **Query structure?** — simplify JOINs, avoid subqueries where JOIN suffices
5. **Data volume?** — archive old data, partition large tables

## Index Rules
- Index foreign keys (they're used in JOINs)
- Composite indexes: column order matters — put high-selectivity columns first
- Covering indexes: include all columns the query needs (avoid table lookups)
- Don't over-index: every index slows down writes
- Monitor index usage: `pg_stat_user_indexes` (PostgreSQL)

## N+1 Prevention
- Use eager loading (JOIN or batch queries)
- Detect with tools like `bullet` (Rails) or `n+1` query detectors
- GraphQL: use DataLoader for batching

## Connection Pool
- Use connection pooling (PgBouncer, external poolers)
- Set appropriate pool sizes: `(core_count * 2) + effective_spindle_count`
- Monitor connection usage — exhausted connections = cascading failures
- Set statement timeouts to prevent runaway queries
