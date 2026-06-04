from pathlib import Path
from auto_skill_mcp.skills.registry import SkillRegistry
from auto_skill_mcp.skills.matcher import SkillMatcher


def test_registry_loads_skills():
    skill_dir = Path(__file__).resolve().parent.parent / "skill_data"
    registry = SkillRegistry(skill_dir=skill_dir)
    assert registry.count() > 0
    skill = registry.get("code-review")
    assert skill is not None
    assert skill.description
    assert skill.body


def test_matcher_returns_results():
    skill_dir = Path(__file__).resolve().parent.parent / "skill_data"
    registry = SkillRegistry(skill_dir=skill_dir)
    matcher = SkillMatcher(registry)
    results = matcher.find_relevant("review code quality", top_k=3)
    assert len(results) > 0
    assert results[0].score > 0
