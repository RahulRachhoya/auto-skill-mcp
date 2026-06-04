---
name: performance-optimization
description: Measure first, optimize only what matters — identify real bottlenecks before making changes.
metadata:
  category: code-quality
  tags: [performance, speed, optimization, profiling]
---

# Performance Optimization

## Golden Rule
**Measure before and after.** Without data, you're guessing. Profile, optimize, re-profile.

## Process
1. **Define the goal** — e.g. "API responds in <200ms p95", "bundle <200KB"
2. **Measure the baseline** — use profiling tools, not intuition
3. **Identify the bottleneck** — is it CPU, I/O, memory, network, database?
4. **Optimize the bottleneck** — the slowest part determines overall speed
5. **Re-measure** — verify improvement, check for regressions
6. **Repeat** — the next bottleneck is now visible

## Common Bottlenecks
- **Database**: N+1 queries, missing indexes, full table scans
- **Network**: serial requests (batch them!), large payloads, no compression
- **Rendering**: unnecessary re-renders, large lists without virtualization
- **Memory**: leaks, excessive allocations, no caching
- **CPU**: inefficient algorithms, tight loops with I/O

## Anti-Patterns
- Optimizing before profiling
- Micro-optimizing (saving 1ms in a function called 5 times)
- Caching without invalidation strategy
- Premature optimization (Knuth: "the root of all evil")
