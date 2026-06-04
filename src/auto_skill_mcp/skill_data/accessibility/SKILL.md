---
name: accessibility
description: Build accessible interfaces — semantic HTML, keyboard navigation, screen reader support, and contrast.
metadata:
  category: frontend
  tags: [accessibility, a11y, inclusive, screen-reader]
---

# Accessibility

## Principles
1. **Semantic HTML** — use the right element (`<button>`, `<nav>`, `<main>`, `<header>`)
2. **Keyboard accessible** — all interactive elements reachable and operable by keyboard
3. **Screen reader friendly** — ARIA labels, roles, and live regions
4. **Color contrast** — WCAG AA minimum (4.5:1 for normal text, 3:1 for large)

## Checklist
- [ ] All images have `alt` text (or `alt=""` for decorative)
- [ ] Form inputs have associated `<label>` elements
- [ ] Focus indicators are visible (never `outline: none` without replacement)
- [ ] Color is not the only way to convey information
- [ ] All functionality works with keyboard alone (Tab, Enter, Escape)
- [ ] ARIA landmarks are used (`role="navigation"`, `role="main"`)
- [ ] Touch targets are at least 44x44px
- [ ] Text can be zoomed to 200% without loss of content

## ARIA Rules
- Don't use ARIA when HTML semantics are sufficient
- Don't override native semantics (e.g., don't add `role="button"` to a `<button>`)
- Use `aria-label` when visible label isn't possible
- Use `aria-live` regions for dynamic content updates
- Test with actual screen readers (VoiceOver, NVDA)
