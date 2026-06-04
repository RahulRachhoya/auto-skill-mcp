# Spec: auto-skill-mcp

## ASSUMPTIONS I'M MAKING
1. The repo lives on GitHub under your account github.com/RahulRachhoya
2. Python 3.12+ is the runtime (confirmed available)
3. git and gh CLI are authenticated and ready
4. The MCP server runs locally via stdio transport (no cloud hosting)
5. All processing is local — no outbound API calls, no LLM calls from the server itself
6. Scikit-learn is acceptable as the only non-stdlib dependency beyond FastMCP
→ Correct any of these or I'll proceed.

## Objective

Build a single local MCP server (`auto-skill-mcp`) that individual developers connect to their agentic coding tool (Claude Code, Cline, Codex, etc.). When the agent starts any task, it calls `analyze_task()` on this server. The server classifies the task intent via TF-IDF keyword matching, finds the most relevant skills from a bundled library (~40 curated SKILL.md files), and returns a structured plan with skill recommendations. The agent can then load full skill content on-demand via `get_skill()`.

**One MCP connection. Zero manual skill management. The agent auto-consults the skill library.**

**User story:** "I'm a solo developer using Claude Code. Instead of installing 40 separate skills from GitHub repos and remembering to invoke `/skill-name`, I connect one MCP server. My agent now automatically consults expert guidance before every task without me doing anything."

**Success looks like:**
- Developer adds one entry to their MCP config
- Agent starts calling `analyze_task()` naturally — the tool description trains it
- Server returns relevant skills ranked by relevance
- Agent loads and applies skill content on-demand

## Tech Stack

| Component | Choice | Version |
|---|---|---|
| Runtime | Python | 3.12+ |
| MCP Framework | FastMCP (via `mcp` package) | Latest |
| Matching Engine | scikit-learn (TfidfVectorizer) | Latest |
| Skill Format | Standard SKILL.md (YAML frontmatter + Markdown) | agentskills.io spec |
| Transport | stdio (local), Streamable HTTP (optional) | |
| Package Manager | pip / uv | |
| Testing | pytest | Latest |

## Commands

```bash
# Install (dev)
pip install -e ".[dev]"

# Run server (stdio)
uv run python -m auto_skill_mcp

# Run server with inspector (testing)
mcp dev src/auto_skill_mcp/server.py

# Test
pytest tests/ -v

# Lint
ruff check src/

# Type check
mypy src/
```

## Project Structure

```
auto-skill-mcp/
├── skill_data/                    # Bundled SKILL.md files
│   ├── code-review/
│   │   └── SKILL.md
│   ├── debugging/
│   │   └── SKILL.md
│   └── ... (~40 skill directories)
├── src/
│   └── auto_skill_mcp/
│       ├── __init__.py
│       ├── __main__.py            # Entry point: `python -m auto_skill_mcp`
│       ├── server.py              # FastMCP app, tool registration
│       ├── models.py              # Skill pydantic model
│       ├── skills/
│       │   ├── __init__.py
│       │   ├── registry.py        # Scan skill_data/, parse frontmatter, build index
│       │   └── matcher.py         # TF-IDF field-weighted matching
│       └── tools/
│           ├── __init__.py
│           ├── analyze_task.py    # Main entry point: classify + match + plan
│           ├── get_skill.py       # Return full SKILL.md body
│           ├── list_skills.py     # Browse catalog
│           └── search_skills.py   # TF-IDF search
├── tests/
│   ├── __init__.py
│   ├── test_registry.py
│   ├── test_matcher.py
│   ├── test_tools.py
│   └── test_server.py
├── pyproject.toml
├── .gitignore
├── .env.example
├── LICENSE                        # MIT
└── README.md
```

## Code Style

- **Python 3.12+** — use `str | None` (not `Optional[str]`), `list[X]` (not `List[X]`)
- **Type hints everywhere** — all functions annotated, return types included
- **Docstrings** — Google-style for tools (the docstring becomes the MCP tool description)
- **No comments in code** — let the code speak; docstrings for public API only
- **Imports** — stdlib first, then third-party, then local (separated by blank line)
- **Line length** — 100 chars max
- **Naming** — `snake_case` for functions/vars, `PascalCase` for classes, `UPPER_CASE` for constants

**Example style:**
```python
from fastmcp import FastMCP
from pydantic import BaseModel

class Skill(BaseModel):
    name: str
    description: str
    category: str
    tags: list[str]
    body: str

mcp = FastMCP("auto-skill-mcp")

@mcp.tool()
def search_skills(query: str, top_k: int = 5) -> list[dict]:
    """Search across all bundled skills using TF-IDF relevance matching.

    Args:
        query: Natural language search query describing what you need.
        top_k: Number of results to return (default 5, max 20).

    Returns:
        List of matched skills with name, description, category, and relevance score.
    """
    return matcher.find_relevant(query, top_k=min(top_k, 20))
```

## Testing Strategy

| Concern | Tool | Location |
|---|---|---|
| Unit tests (matcher, registry) | pytest | `tests/test_matcher.py`, `tests/test_registry.py` |
| Tool integration tests | pytest | `tests/test_tools.py` |
| Server smoke test | MCP Inspector | Manual (`mcp dev src/auto_skill_mcp/server.py`) |

- Tests are auto-discovered by pytest via `tests/` directory
- No external dependencies in tests — all skill data is bundled
- Matcher tests use real skill data to verify ranking quality
- Tool tests mock the registry and verify JSON-RPC output shape
- No coverage threshold initially (small project); aim for >80%

## Boundaries

**Always do:**
- Write type hints for every function
- Validate tool inputs (use type hints + pydantic)
- Write tests for every new tool or matcher change
- Follow Conventional Commits format for git messages
- Keep skill content under 500 lines per SKILL.md
- Run `ruff check src/` before committing

**Ask first:**
- Adding new Python dependencies beyond fastmcp, scikit-learn, pytest, ruff
- Changing the SKILL.md format or adding new frontmatter fields
- Restructuring the directory layout
- Changing transport from stdio to HTTP
- Adding any outbound network calls

**Never do:**
- Commit API keys or secrets (keep in `.env` or env vars)
- Make outbound network calls from the MCP server
- Store user data or write files to disk
- Remove failing tests without approval
- Modify `skill_data/` structure without updating the registry

## Success Criteria

- [ ] `tools/list` returns all 4 tools with correct names and descriptions
- [ ] `search_skills(query)` returns ranked results using TF-IDF
- [ ] `get_skill(name)` returns full SKILL.md body
- [ ] `analyze_task(context, goal)` classifies intent, matches skills, returns structured plan
- [ ] All ~40 skills are parseable and load without errors
- [ ] `pytest tests/ -v` passes all tests
- [ ] `ruff check src/` passes with zero warnings
- [ ] `mypy src/` passes with zero errors
- [ ] Package installs via `pip install -e .`
- [ ] Server runs via `python -m auto_skill_mcp`

## Open Questions
None resolved in prior conversation. All decisions captured above.
