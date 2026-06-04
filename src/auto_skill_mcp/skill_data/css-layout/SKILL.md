---
name: css-layout
description: Build responsive, maintainable layouts with CSS Grid, Flexbox, and consistent spacing.
metadata:
  category: frontend
  tags: [css, layout, grid, flexbox, responsive]
---

# CSS Layout

## Modern Layout
- **Flexbox**: one-dimensional layouts (row or column). Great for navs, cards, centering
- **CSS Grid**: two-dimensional layouts. Great for page structure, dashboards
- Use both together: Grid for page layout, Flexbox for component-level layout

## Grid Template
```css
.app-layout {
  display: grid;
  grid-template-areas:
    "sidebar main"
    "sidebar footer";
  grid-template-columns: 250px 1fr;
  grid-template-rows: 1fr auto;
  min-height: 100vh;
}
```

## Responsive Design
- Mobile-first: base styles for mobile, `@media (min-width: ...)` for larger screens
- Use `clamp()` for fluid typography: `font-size: clamp(1rem, 2.5vw, 1.5rem)`
- Use `min/max-width/height` instead of fixed widths where possible
- Test on real devices, not just browser DevTools resize

## Spacing
- Use a spacing scale (4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px)
- Use `gap` in Flexbox/Grid instead of margin hacks
- Use logical properties (`margin-inline`, `padding-block`) for RTL support
