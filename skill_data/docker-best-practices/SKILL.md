---
name: docker-best-practices
description: Build efficient, secure Docker images — minimize layers, reduce size, follow security best practices.
metadata:
  category: devops
  tags: [docker, container, image, build, security]
---

# Docker Best Practices

## Image Size
- Use slim/base images (`python:3.12-slim`, not `python:3.12`)
- Multi-stage builds — build in one stage, copy artifacts to final stage
- Combine RUN commands (`&&`) to reduce layers
- Remove package manager caches in the same layer
- `.dockerignore` to exclude unnecessary files

## Dockerfile
```dockerfile
FROM python:3.12-slim AS builder
WORKDIR /app
COPY pyproject.toml .
RUN pip install --user --no-cache-dir -e .

FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY src/ src/
COPY skill_data/ skill_data/
ENV PATH=/root/.local/bin:$PATH
CMD ["python", "-m", "auto_skill_mcp"]
```

## Security
- Don't run as root — use `USER appuser`
- Don't store secrets in images — use build args or mount secrets
- Scan images with `docker scan` or `trivy`
- Pin base image versions (don't use `:latest`)
- Use read-only root filesystem where possible
