---
name: api-design
description: Design stable, consistent, and discoverable APIs with clear contracts and predictable behavior.
metadata:
  category: architecture
  tags: [api, design, rest, contract, consistency]
---

# API Design

## Principles
1. **Consistency** — same patterns everywhere (naming, error format, pagination)
2. **Backward compatibility** — never break existing clients. Add, don't change
3. **Explicit contracts** — clearly document what each endpoint accepts and returns
4. **Least surprise** — follow framework conventions, standard HTTP methods, status codes

## REST Design Rules
- Use nouns for resources (`/users`, `/orders`), not verbs (`/getUsers`)
- Use HTTP methods: GET (read), POST (create), PUT (replace), PATCH (update), DELETE (remove)
- Plural resource names: `/users` not `/user`
- Nested resources for relationships: `/users/123/orders`
- Version via header or prefix: `Accept: application/vnd.api.v2+json` or `/api/v2/`

## Response Structure
```json
{
  "data": { ... },
  "meta": { "page": 1, "total": 42 },
  "error": null
}
```
- Consistent error format: `{ "error": { "code": "VALIDATION_ERROR", "message": "...", "details": [...] } }`
- Use standard HTTP status codes: 200, 201, 204, 400, 401, 403, 404, 409, 422, 500
