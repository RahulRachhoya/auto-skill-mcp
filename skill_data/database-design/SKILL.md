---
name: database-design
description: Design efficient, maintainable database schemas with proper normalization, indexes, and constraints.
metadata:
  category: architecture
  tags: [database, schema, sql, design, normalization]
---

# Database Design

## Normalization (3NF)
1. **1NF**: atomic columns, no repeated groups
2. **2NF**: 1NF + every non-key column depends on the whole primary key
3. **3NF**: 2NF + no transitive dependencies (non-key depends on another non-key)

## Index Strategy
- Primary key gets a unique index (auto)
- Foreign keys should be indexed
- Columns used in WHERE, JOIN, ORDER BY, GROUP BY are candidates
- Don't over-index: writes get slower with every index
- Use composite indexes for multi-column queries (column order matters)

## Common Patterns
- **Soft deletes**: add `deleted_at` column, filter in queries
- **Created/updated timestamps**: always include `created_at`, `updated_at`
- **UUIDs vs auto-increment**: UUIDs for distributed systems, auto-increment for single-DB
- **Enum types**: use check constraints or lookup tables, not raw strings
- **JSON columns**: use only when schema is truly dynamic (prefer normalized columns)

## Anti-Patterns
- Storing comma-separated values in a single column
- Using text for numeric or date values
- No foreign key constraints
- Indexing every column "just in case"
- Giant migration files that mix schema and data changes
