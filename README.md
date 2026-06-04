# auto-skill-mcp

One MCP server that auto-serves skills to agentic coding tools. Connect once, get expert guidance on any task.

## Quick start

```bash
pip install auto-skill-mcp

# or with uv
uvx auto-skill-mcp
```

## Agent configuration

Add to your MCP config (e.g. `claude_desktop_config.json`, `.cursor/config.json`, or `.vscode/mcp.json`):

```json
{
  "mcpServers": {
    "auto-skill-mcp": {
      "command": "uvx",
      "args": ["auto-skill-mcp"]
    }
  }
}
```

## How it works

Your coding agent calls `analyze_task()` at the start of any task. The server classifies the task intent via TF-IDF matching, finds the most relevant skills from a bundled library (~43 curated guides), and returns a structured plan with recommendations.

No manual skill installation. No `/skill-name` commands to remember. One connection.

## Tools

| Tool | Description |
|---|---|
| `analyze_task` | [REQUIRED] Call first — classifies intent, returns plan + matched skills |
| `get_skill` | Load full SKILL.md body for a specific skill |
| `list_skills` | Browse all skills, optionally filtered by category |
| `search_skills` | Search skills by keyword or topic |

### Typical flow

```text
1. agent calls analyze_task("review PR #42", goal="find security bugs")
   → task_type: "security", complexity: "medium"
   → recommends: security-audit, code-review, testing
2. agent calls get_skill("security-audit")
   → gets full guidance on security review process
3. agent uses the guidance to perform the task
```

## Skills included (~43)

| Category | Skills |
|---|---|
| **Code quality** | code-review, debugging, testing, refactoring, code-simplification, error-handling, technical-debt-management, performance-optimization |
| **Architecture & security** | api-design, database-design, architecture-decisions, dependency-management, security-audit, secrets-management, input-validation, authentication-patterns |
| **DevOps & git** | ci-cd-setup, docker-best-practices, monitoring-setup, incident-response, migration-planning, git-workflow, commit-messages, pr-description |
| **Frontend & backend** | react-patterns, css-layout, accessibility, state-management, form-design, rest-api-design, graphql-patterns, webhook-design, rate-limiting |
| **Docs & general** | writing-docs, api-documentation, readme-crafting, adr-writing, caching-strategies, bundle-optimization, query-optimization, changelog-generation, pair-programming, on-call-handbook |

## Development

```bash
pip install -e ".[dev]"
pytest tests/ -v
ruff check src/ tests/
mypy src/auto_skill_mcp/
```

## License

MIT
