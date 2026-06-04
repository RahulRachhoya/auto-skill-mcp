# auto-skill-mcp

One MCP server that auto-serves skills to agentic coding tools. Connect once,
get expert guidance on any task.

## Quick start

```bash
# Install globally
pip install auto-skill-mcp

# Or run directly with uv (no install needed)
uvx auto-skill-mcp
```

## Auto-installer

Detect and configure your coding agents automatically:

```bash
# Scan for agents and preview changes
auto-skill-mcp install --dry-run

# Install to all detected agents
auto-skill-mcp install

# List detected agents and their config files
auto-skill-mcp list

# Remove from all agents
auto-skill-mcp uninstall

# Start the MCP server (default, same as `uvx auto-skill-mcp`)
auto-skill-mcp
```

The installer detects these agents across global and project scope:
- **Global:** Claude Desktop, Claude Code, Cursor, Windsurf, Cline, Roo Code,
  OpenCode, Gemini CLI, GitHub Copilot CLI
- **Project:** VS Code `.vscode/mcp.json`, JetBrains `.idea/mcp.json`,
  Claude Code `.mcp.json`, Cursor `.cursor/mcp.json`

## Manual configuration

Add to your MCP config (`claude_desktop_config.json`, `.cursor/mcp.json`,
`.vscode/mcp.json`, etc.):

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

Your coding agent calls `analyze_task()` at the start of any task. The server
classifies the task intent via TF-IDF matching, finds the most relevant skills
from a bundled library (43 curated guides), and returns a structured plan with
recommendations. No manual skill installation — one connection.

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

## Skills included (43)

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
