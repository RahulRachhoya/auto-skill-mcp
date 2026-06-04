from auto_skill_mcp.skills.matcher import SkillMatcher
from auto_skill_mcp.skills.registry import SkillRegistry


def make_search_skills(registry: SkillRegistry):
    matcher = SkillMatcher(registry)

    def search_skills(query: str, top_k: int = 5) -> list[dict]:
        """Search across all bundled skills using TF-IDF relevance matching.

        Args:
            query: Natural language search query describing what you need.
            top_k: Number of results to return (default 5, max 20).

        Returns:
            Ranked list of matched skills with name, description, category, and score.
        """
        results = matcher.find_relevant(query, top_k=min(top_k, 20))
        return [r.model_dump() for r in results]

    return search_skills
