---
name: graphql-patterns
description: Design resolvers, handle N+1, manage mutations, and structure your schema effectively.
metadata:
  category: backend
  tags: [graphql, api, schema, resolver, query]
---

# GraphQL Patterns

## Schema Design
- **Describe data, not actions** — nouns in types, verbs in mutations
- **Use interfaces and unions** for polymorphic relationships
- **Nullable by default** — only mark required if it's truly always present
- **Paginate lists** — always use connection types for list fields

## N+1 Prevention
```graphql
# Bad: N+1 queries
type User {
  posts: [Post]  # Fetches posts for each user individually
}

# Good: use DataLoader
const postLoader = new DataLoader(ids =>
  db.posts.findAll({ where: { userId: { in: ids } } })
)
```

## Mutations
- Single responsibility per mutation
- Return the mutated object (so the client can update its cache)
- Input types end with `Input`: `CreateUserInput`
- Use optimistic updates for fast UX (revert on error)

## Security
- Depth limiting (prevent deeply nested queries)
- Complexity scoring (costly fields have higher weight)
- Rate limiting at the query level
- Auth checked in every resolver, not middleware
- Query whitelisting for production APIs (persisted queries)
