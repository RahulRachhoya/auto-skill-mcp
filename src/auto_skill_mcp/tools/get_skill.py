from auto_skill_mcp.skills.registry import SkillRegistry


def make_get_skill(registry: SkillRegistry):
    def get_skill(skill_name: str) -> str:
        """Load the full content of a specific skill by name.

        Args:
            skill_name: The skill name (e.g. "code-review", "debugging", "testing").

        Returns:
            Full SKILL.md body with instructions and guidance.
        """
        skill = registry.get(skill_name)
        if skill is None:
            return f"Skill '{skill_name}' not found. Use list_skills() to see all available skills."
        return skill.body

    return get_skill
