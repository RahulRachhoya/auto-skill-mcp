---
name: rate-limiting
description: Implement rate limiting to protect APIs from abuse — per-user, per-IP, and global limits.
metadata:
  category: backend
  tags: [rate-limiting, throttling, api, protection]
---

# Rate Limiting

## Strategies
| Strategy | How | Use Case |
|----------|-----|----------|
| Token bucket | Tokens refill at fixed rate | Bursty traffic, API keys |
| Leaky bucket | Fixed processing rate | Queue processing |
| Sliding window | Count requests in rolling time window | General purpose |
| Fixed window | Reset counter at intervals | Simple rate limiting |

## Implementation
```python
# Sliding window with Redis
import time
from redis import Redis

r = Redis()
def check_rate_limit(user_id: str, max_requests: int = 100, window: int = 60) -> bool:
    key = f"ratelimit:{user_id}:{int(time.time() / window)}"
    count = r.incr(key)
    if count == 1:
        r.expire(key, window * 2)
    return count <= max_requests
```

## Response Headers
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 42
X-RateLimit-Reset: 1680000000
Retry-After: 30
```

## Rules
- Rate limit at the API gateway level, not just application level
- Return 429 Too Many Requests with a Retry-After header
- Log rate limit violations for abuse analysis
- Allow higher limits for authenticated users vs anonymous
- Queue or degrade gracefully instead of hard-failing where possible
