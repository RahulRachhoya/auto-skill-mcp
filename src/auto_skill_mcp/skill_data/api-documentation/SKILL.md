---
name: api-documentation
description: Document APIs clearly — every endpoint, parameter, response, and error code with examples.
metadata:
  category: documentation
  tags: [api, docs, openapi, swagger, reference]
---

# API Documentation

## What Every Endpoint Needs
- **Description** — what does this endpoint do? When would you use it?
- **Path and method** — `GET /api/v1/users/{id}`
- **Parameters** — path params, query params, headers, body (name, type, required, default, description)
- **Request example** — a complete, working request (curl or code)
- **Response example** — the full response body, with explanations
- **Error codes** — what errors can this endpoint return and why?
- **Authentication** — is auth required? What type?

## OpenAPI Format
```yaml
paths:
  /users/{id}:
    get:
      summary: Retrieve a user
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
      responses:
        "200":
          description: User found
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/User"
        "404":
          description: User not found
```

## Rules
- Keep the docs in sync with the code (auto-generate from OpenAPI when possible)
- Document breaking changes prominently in changelog
- Version the docs alongside the API
- Include rate limits, pagination defaults, and timeout values
- Test every code example (copy-paste should work)
