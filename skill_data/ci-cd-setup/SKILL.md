---
name: ci-cd-setup
description: Set up continuous integration and delivery pipelines with automated quality gates and safe deployments.
metadata:
  category: devops
  tags: [ci, cd, pipeline, automation, deployment]
---

# CI/CD Setup

## Pipeline Stages
1. **Lint** — style checks, formatting, static analysis
2. **Type check** — mypy, TypeScript compiler
3. **Test** — unit tests, integration tests, coverage report
4. **Build** — compile, bundle, containerize
5. **Security scan** — dependency audit, SAST, secrets scan
6. **Deploy** — staging → automated tests → production (with manual gate)

## Quality Gates
- All tests must pass
- Lint must be clean
- No new critical/high vulnerabilities
- Test coverage doesn't decrease
- Build succeeds

## Deployment Strategies
- **Blue-green**: two identical environments, switch traffic
- **Canary**: roll out to small percentage first, monitor, then full rollout
- **Feature flags**: deploy code disabled, enable per-user/group
- **Rollback plan**: every deployment has a tested rollback

## CI Config
```yaml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install -e ".[dev]"
      - run: ruff check src/
      - run: pytest tests/ -v
```
