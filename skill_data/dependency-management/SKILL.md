---
name: dependency-management
description: Manage third-party dependencies intentionally — minimize, pin versions, audit regularly.
metadata:
  category: architecture
  tags: [dependencies, packages, security, supply-chain]
---

# Dependency Management

## Principles
1. **Minimize dependencies** — every dependency is a risk (security, maintenance, breaking changes)
2. **Pin versions** — lockfiles ensure reproducible builds
3. **Audit regularly** — run `pip audit` / `npm audit` / `cargo audit` in CI
4. **Prefer maintained** — check last commit date, issue response time, number of maintainers

## Evaluation Criteria
Before adding a dependency, ask:
- What does this give us that we can't write in <50 lines?
- Is it actively maintained? (recent commits, open issues with responses)
- Does it have a compatible license?
- What is the download/usage footprint?
- What is the security track record?

## Management Process
- Use a lockfile (`poetry.lock`, `package-lock.json`, `Cargo.lock`)
- Run `pip audit` / `npm audit` / `cargo audit` in CI
- Review major version upgrades for breaking changes
- Remove unused dependencies (use tools like `deptrace`, `depcheck`)
- Keep a bill of materials document for compliance

## Version Strategy
- App/library pinning: pin exact versions for apps, use caret ranges for libraries
- Security patches: apply promptly, especially for critical vulnerabilities
- Major upgrades: plan, test, and migrate deliberately — never upgrade major versions in a bug fix
