from auto_skill_mcp.skills.registry import SkillRegistry


def make_list_skills(registry: SkillRegistry):
    def list_skills(category: str | None = None) -> list[dict]:
        """Browse all available skills, optionally filtered by category.

        Args:
            category: Optional category filter (e.g. "code-quality", "security", "devops").

        Returns:
            List of skill metadata: name, description, category, and tags.
        """
        skills = registry.get_all()
        if category:
            skills = [s for s in skills if s.category == category]
        return [
            {
                "name": s.name,
                "description": s.description,
                "category": s.category,
                "tags": s.tags,
            }
            for s in sorted(skills, key=lambda x: x.name)
        ]

    return list_skills
