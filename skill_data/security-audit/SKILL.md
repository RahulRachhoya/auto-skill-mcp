---
name: security-audit
description: Perform systematic security audits covering OWASP Top 10, dependency vulnerabilities, and data protection.
metadata:
  category: security
  tags: [security, audit, owasp, vulnerability]
---

# Security Audit

## OWASP Top 10 Checklist
- [ ] **Broken Access Control** — verify auth on every endpoint, test role escalation
- [ ] **Cryptographic Failures** — no plaintext secrets, HTTPS everywhere, proper hashing
- [ ] **Injection** — parameterized queries, input sanitization, output encoding
- [ ] **Insecure Design** — rate limiting, proper error messages (no stack traces to users)
- [ ] **Security Misconfiguration** — default creds changed, CORS locked down, debug mode off
- [ ] **Vulnerable Components** — run dependency audit, check CVEs
- [ ] **Auth Failures** — MFA where applicable, session timeout, password policies
- [ ] **Data Integrity Failures** — CSRF tokens, signed cookies, integrity checks
- [ ] **Logging Failures** — audit log of sensitive actions, no secrets in logs
- [ ] **SSRF** — validate/restrict outbound URLs, don't forward internal responses

## Process
1. Map the attack surface (all entry points: API, UI, files, queues)
2. Threat model each entry point (who can access, what can go wrong)
3. Test controls (auth, validation, encryption)
4. Scan dependencies for CVEs
5. Review secrets management (env vars, vault, no hardcoded keys)
6. Document findings with severity, reproduction steps, and fix guidance
