---
name: input-validation
description: Validate all external inputs — never trust user data, API responses, or file contents.
metadata:
  category: security
  tags: [validation, input, security, sanitization]
---

# Input Validation

## Rules
1. **Validate early** — at the boundary (API handler, form submit, file read)
2. **Validate strictly** — whitelist allowed values, don't blacklist bad ones
3. **Validate every input** — request params, headers, body, file uploads, webhook payloads
4. **Reject invalid, don't sanitize** — reject early with clear error messages

## What to Validate
- **Type**: is it the expected type (string, int, boolean)?
- **Format**: does it match the expected pattern (email, URL, phone)?
- **Range**: is the value within acceptable bounds (min/max length, min/max value)?
- **Presence**: is it required or optional?
- **Uniqueness**: does it conflict with existing data?

## Common Validations
```python
from pydantic import BaseModel, EmailStr, Field, validator

class UserInput(BaseModel):
    email: EmailStr
    age: int = Field(ge=0, le=150)
    name: str = Field(min_length=1, max_length=100)

    @validator("name")
    def no_xss(cls, v):
        if "<script" in v.lower():
            raise ValueError("Invalid characters in name")
        return v
```

## Anti-Patterns
- Client-side validation only (always validate server-side)
- "Sanitize" instead of reject (silently changing input hides bugs)
- Using regex for complex validation (email, URLs — use dedicated libraries)
- Trusting file extensions for file type validation (check magic bytes)
