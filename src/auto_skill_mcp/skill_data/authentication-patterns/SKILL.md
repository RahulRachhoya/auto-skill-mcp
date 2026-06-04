---
name: authentication-patterns
description: Implement authentication and authorization securely — hashing, sessions, tokens, and permissions.
metadata:
  category: security
  tags: [auth, authentication, authorization, security]
---

# Authentication Patterns

## Password Handling
- **Hash, don't encrypt** — use bcrypt, argon2, or scrypt. Never SHA-1/MD5
- **Salt every password** — unique salt per user (automatic with bcrypt/argon2)
- **Minimum requirements** — 8+ chars, no arbitrary complexity rules (those reduce entropy)
- **Rate limit login attempts** — prevent brute force

## Session vs Token Auth
| Aspect | Session | JWT |
|--------|---------|-----|
| State | Server-side | Client-side (stateless) |
| Storage | Cookie (HttpOnly) | LocalStorage / header |
| Revocation | Immediate | Until expiration (need blocklist) |
| Scaling | Shared session store needed | Built-in |
| Payload | Session ID only | Can include claims |

## Authorization
- **RBAC** — roles assigned to users, permissions assigned to roles
- **Attribute-based (ABAC)** — permissions based on user, resource, and context attributes
- **Least privilege** — grant minimum permissions needed

## Common Vulnerabilities
- JWT with `alg: none` — always verify the algorithm
- Tokens in URL parameters — use Authorization header
- No expiry on tokens — always set expiration, use refresh tokens
- Session fixation — regenerate session ID on login
- Missing 2FA/MFA on sensitive operations
