---
name: caching-strategies
description: Cache effectively — in-memory, distributed, HTTP caching — with proper invalidation.
metadata:
  category: general
  tags: [cache, performance, redis, memory, invalidation]
---

# Caching Strategies

## Cache Levels
| Level | Storage | Speed | Use Case |
|-------|---------|-------|----------|
| L1 (in-memory) | Application RAM | <1ms | Hot data, repeated queries |
| L2 (distributed) | Redis/Memcached | 1-5ms | Shared across instances |
| L3 (HTTP/CDN) | Browser/CDN | 10-100ms | Static assets, API responses |

## Caching Patterns
- **Cache-aside**: read from cache, miss → read DB → write to cache → return
- **Write-through**: write to cache first, then DB
- **Write-behind**: write to cache, async write to DB
- **Cache invalidation**: the hardest problem — use TTLs, version keys, or event-driven purges

## HTTP Caching
- Use `Cache-Control` headers: `public`, `private`, `max-age`, `no-cache`, `no-store`
- Use ETags for conditional requests
- Set appropriate TTLs: static assets (1 year with hash in URL), API responses (seconds to minutes)

## Rules
- Cache the result of expensive operations (DB queries, API calls, computation)
- Never cache sensitive data (PII, auth tokens)
- Always set a TTL (even if long) — prevent stale data
- Monitor cache hit rates — low hit rate means wrong cache strategy
- Have a cache warming strategy for critical data
