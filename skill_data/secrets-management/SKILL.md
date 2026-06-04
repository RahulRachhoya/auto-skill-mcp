---
name: secrets-management
description: Store, rotate, and audit secrets securely — never hardcode, never commit, never share.
metadata:
  category: security
  tags: [secrets, credentials, keys, vault, security]
---

# Secrets Management

## Rules
1. **Never hardcode secrets** — no API keys, passwords, or tokens in source code
2. **Never commit secrets** — add `.env` to `.gitignore`, use pre-commit hooks to scan
3. **Use environment variables** — read secrets from env at runtime, not from config files
4. **Rotate regularly** — rotate keys every 90 days, immediately on suspected breach

## Methods
| Method | Use Case | Example |
|--------|----------|---------|
| Env vars | Development, simple deployments | `DB_PASSWORD=xxx` in `.env` (not committed) |
| Secret manager | Production | AWS Secrets Manager, HashiCorp Vault |
| CI/CD secrets | Pipeline jobs | GitHub Actions secrets, GitLab CI variables |
| Signed URLs | Short-lived access | S3 presigned URLs, JWT tokens |

## Detection
- Use `git secrets` or `truffleHog` as pre-commit hooks
- Scan repos for accidental commits with `git log -p --all | grep -i "api_key\|password\|secret"`
- If a secret is committed: rotate it immediately, then use `git filter-repo` to scrub
