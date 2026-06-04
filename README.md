# auto-skill-mcp

One MCP server that auto-serves skills to agentic coding tools. Connect once, get expert guidance on any task.

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

Your coding agent (Claude Code, Cline, etc.) calls `analyze_task()` at the start of any task. The server classifies the task intent via TF-IDF matching, finds the most relevant skills from a bundled library (~40 curated guides), and returns a structured plan with recommendations.

No manual skill installation. No `/skill-name` commands to remember. One connection.

## Tools

| Tool | Description |
|---|---|
| `analyze_task` | Classify task intent, return plan + matched skills. Call this first. |
| `get_skill` | Load full SKILL.md body for a specific skill. |
| `list_skills` | Browse all available skills, optionally by category. |
| `search_skills` | Search skills by keyword or topic. |

## Quick start

```bash
# Install
pip install auto-skill-mcp

# Run
python -m auto_skill_mcp

# Or with uvx (no install)
uvx auto-skill-mcp
```

## Development

```bash
pip install -e ".[dev]"
pytest tests/ -v
ruff check src/
```

## License

MIT
