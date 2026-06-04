from pathlib import Path

from fastmcp import FastMCP

from auto_skill_mcp.skills.registry import SkillRegistry
from auto_skill_mcp.tools.analyze_task import make_analyze_task
from auto_skill_mcp.tools.get_skill import make_get_skill
from auto_skill_mcp.tools.list_skills import make_list_skills
from auto_skill_mcp.tools.search_skills import make_search_skills

mcp = FastMCP("auto-skill-mcp")

_skill_dir = Path(__file__).resolve().parent.parent.parent / "skill_data"
_registry = SkillRegistry(skill_dir=_skill_dir)


@mcp.tool()
def ping() -> str:
    """Health check — returns pong if server is running."""
    return "pong"


mcp.tool(name="list_skills")(make_list_skills(_registry))
mcp.tool(name="search_skills")(make_search_skills(_registry))
mcp.tool(name="get_skill")(make_get_skill(_registry))
mcp.tool(name="analyze_task")(make_analyze_task(_registry))


def main() -> None:
    mcp.run()
