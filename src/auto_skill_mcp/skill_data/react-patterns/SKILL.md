---
name: react-patterns
description: Build React components with proper composition, state management, and performance patterns.
metadata:
  category: frontend
  tags: [react, components, hooks, state, performance]
---

# React Patterns

## Component Design
- **Single responsibility**: one component, one concern
- **Composition over props**: compound components pattern instead of boolean props
- **Presentational vs container**: separate rendering from logic
- **Small components**: if it's >100 lines, extract

## Hooks Rules
- Only call hooks at the top level (not in conditions, loops, callbacks)
- Only call hooks from React functions
- `useEffect` dependencies must be exhaustive (use the linter rule)
- Custom hooks start with `use` and compose primitive hooks

## Performance
- `React.memo` for pure components that re-render often with same props
- `useMemo`/`useCallback` for expensive computations (measure first!)
- Virtualize long lists (`react-window`, `react-virtuoso`)
- Lazy load routes and heavy components (`React.lazy`, `Suspense`)
- Avoid passing new objects/arrays as props (use `useMemo` or stable references)

## State Management
- **Local state first**: `useState` > `useReducer` > context > external library
- **Context** for shared global state (theme, auth, locale)
- **Zustand/Redux** only when state logic is truly complex or shared across many components
- Colocate state with the component that needs it
