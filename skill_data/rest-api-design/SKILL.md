---
name: rest-api-design
description: Design RESTful APIs that are consistent, predictable, and easy to consume.
metadata:
  category: backend
  tags: [rest, api, http, endpoints, design]
---

# REST API Design

## URL Structure
- `/api/v1/resources` — versioned, plural nouns
- `/api/v1/resources/123` — single resource by ID
- `/api/v1/resources/123/relationships` — sub-resources
- Query params for filtering, sorting, pagination: `?status=active&sort=-created_at&page=2&per_page=20`

## HTTP Methods & Status Codes
| Method | Action | Success | Error |
|--------|--------|---------|-------|
| GET | List | 200 | — |
| GET | Retrieve | 200 | 404 |
| POST | Create | 201 | 400, 422 |
| PUT | Replace | 200 | 404, 400 |
| PATCH | Partial update | 200 | 404, 422 |
| DELETE | Remove | 204 | 404 |

## Response Format
```json
{
  "data": { ... },
  "meta": { "page": 1, "per_page": 20, "total": 100 },
  "error": null
}
```

## Error Format
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid email address",
    "details": [
      { "field": "email", "message": "must be a valid email", "code": "invalid_format" }
    ]
  }
}
```

## Pagination
- Use cursor-based pagination for large datasets (stable under writes)
- Use offset-based for simpler cases (small datasets, admin UIs)
- Return `next_cursor` or `next_page` in response meta
- Default page size, enforce max page size
