---
name: bundle-optimization
description: Optimize JavaScript bundles — code splitting, tree shaking, and dependency analysis.
metadata:
  category: general
  tags: [bundle, webpack, vite, size, optimization]
---

# Bundle Optimization

## Strategies
1. **Code splitting** — split by route, component, or library. Load on demand
2. **Tree shaking** — remove unused exports. Only import what you need
3. **Dependency analysis** — find large or duplicate dependencies (`webpack-bundle-analyzer`)
4. **Lazy loading** — load heavy components only when needed (`React.lazy`, dynamic imports)
5. **Compression** — enable gzip/brotli at the server/CDN level

## Targets
- Initial JS bundle: <200KB (gzipped)
- Initial CSS bundle: <50KB (gzipped)
- Time to interactive: <3s on 4G

## Techniques
```javascript
// Good: code-split by route
const Dashboard = () => import('./Dashboard')

// Good: import only what you need
import { format } from 'date-fns'  // not `import dateFns from 'date-fns'`

// Bad: whole library import
import _ from 'lodash'
```

## Tooling
- `webpack-bundle-analyzer` / `vite-bundle-analyzer` — visualize bundle composition
- `bundlesize` / `size-limit` — enforce bundle size budgets in CI
- `purgecss` — remove unused CSS
- Use ES modules for better tree shaking
