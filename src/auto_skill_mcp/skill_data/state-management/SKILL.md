---
name: state-management
description: Manage application state predictably — local state first, lifting when needed, libraries only as last resort.
metadata:
  category: frontend
  tags: [state, management, react, redux, context]
---

# State Management

## Decision Tree
1. Can this be derived from existing state? → **derived state** (no new state needed)
2. Is it used by one component? → **useState** (local state)
3. Is it used by a small subtree? → **prop drilling** (simple case) or **useContext**
4. Is it complex (multi-step, undo/redo)? → **useReducer**
5. Is it used across many unrelated components? → **external library** (Zustand, Redux, Jotai)

## Rules
- Single source of truth for each piece of state
- State should be minimized — derive what you can
- Server state (API data) is different from UI state — use React Query/SWR for server state
- Don't put computed values in state — compute them during render

## Patterns
```typescript
// Good: derive from state
const [items, setItems] = useState<Item[]>([])
const totalPrice = useMemo(() =>
  items.reduce((sum, i) => sum + i.price, 0),
  [items]
)

// Bad: redundant state
const [items, setItems] = useState<Item[]>([])
const [totalPrice, setTotalPrice] = useState(0) // derived from items!
```
