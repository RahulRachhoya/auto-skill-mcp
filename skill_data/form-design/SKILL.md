---
name: form-design
description: Design forms that users can complete — clear validation, helpful errors, accessible inputs, and good UX.
metadata:
  category: frontend
  tags: [form, design, validation, ux, input]
---

# Form Design

## UX Rules
- **Single column** layouts are faster to complete than multi-column
- **Group related fields** with clear section headers
- **Show requirements before** the user starts typing (not as an error after)
- **Inline validation** — validate on blur, not on every keystroke
- **Clear error messages** — what's wrong and how to fix it, not just "invalid input"

## Validation
- Validate on submit AND on blur for a good UX
- Disable submit button while submitting (prevent double-submit)
- Show all errors at once, not one at a time
- Preserve user input on validation error (don't clear the form)

## Accessibility
- Every input has a `<label>` (not placeholder as label)
- Error messages linked to inputs via `aria-describedby`
- Required fields are clearly marked
- Tab order follows visual order
- Auto-focus the first field (but don't steal focus from screen readers)

## Data Handling
- Use a schema validation library (Zod, Yup, Pydantic)
- Serialize form data on submit (don't rely on DOM values)
- Handle loading, success, and error states
- Consider optimistic UI for fast feedback
