from pathlib import Path

from auto_skill_mcp.skills.registry import SkillRegistry
from auto_skill_mcp.tools.analyze_task import make_analyze_task
from auto_skill_mcp.tools.get_skill import make_get_skill
from auto_skill_mcp.tools.list_skills import make_list_skills
from auto_skill_mcp.tools.search_skills import make_search_skills

SKILL_DIR = Path(__file__).resolve().parent.parent / "skill_data"


def test_list_skills():
    registry = SkillRegistry(skill_dir=SKILL_DIR)
    list_skills = make_list_skills(registry)
    result = list_skills(category=None)
    assert isinstance(result, list)
    assert len(result) > 0
    assert "name" in result[0]
    assert "description" in result[0]


def test_list_skills_by_category():
    registry = SkillRegistry(skill_dir=SKILL_DIR)
    list_skills = make_list_skills(registry)
    result = list_skills(category="code-quality")
    assert all(s["category"] == "code-quality" for s in result)


def test_search_skills():
    registry = SkillRegistry(skill_dir=SKILL_DIR)
    search_skills = make_search_skills(registry)
    result = search_skills("review code", top_k=3)
    assert isinstance(result, list)
    if result:
        assert "score" in result[0]
        assert result[0]["score"] > 0


def test_get_skill_found():
    registry = SkillRegistry(skill_dir=SKILL_DIR)
    get_skill = make_get_skill(registry)
    result = get_skill("code-review")
    assert isinstance(result, str)
    assert len(result) > 10


def test_get_skill_not_found():
    registry = SkillRegistry(skill_dir=SKILL_DIR)
    get_skill = make_get_skill(registry)
    result = get_skill("nonexistent-skill")
    assert "not found" in result


def test_analyze_task():
    registry = SkillRegistry(skill_dir=SKILL_DIR)
    analyze_task = make_analyze_task(registry)
    result = analyze_task("review a pull request for bugs", goal="ensure code quality")
    assert result["task_type"] == "code-review"
    assert "complexity" in result
    assert "recommended_skills" in result
    assert "suggested_approach" in result


def test_analyze_task_general():
    registry = SkillRegistry(skill_dir=SKILL_DIR)
    analyze_task = make_analyze_task(registry)
    result = analyze_task("build a new feature")
    assert result["task_type"] == "general"
