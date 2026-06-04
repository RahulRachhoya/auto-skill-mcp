import re

from auto_skill_mcp.models import MatchedSkill, TaskAnalysis
from auto_skill_mcp.skills.matcher import SkillMatcher
from auto_skill_mcp.skills.registry import SkillRegistry

TASK_TYPES: dict[str, list[str]] = {
    "code-review": ["review", "pull request", "code review", "merge"],
    "debugging": ["bug", "error", "crash", "not working", "fix", "broken", "issue"],
    "testing": ["test", "coverage", "spec", "assert", "mock"],
    "refactoring": ["refactor", "clean up", "restructure", "technical debt"],
    "architecture": ["architecture", "design", "schema", "system design", "database"],
    "security": ["security", "vulnerability", "auth", "permission", "owasp"],
    "performance": ["performance", "slow", "latency", "optimize", "bottleneck"],
    "documentation": ["document", "readme", "docs", "api docs", "comment"],
    "devops": ["deploy", "ci", "cd", "pipeline", "docker", "infrastructure"],
    "frontend": ["ui", "component", "css", "frontend", "react", "vue", "angular", "tailwind"],
    "backend": ["api", "endpoint", "backend", "rest", "graphql", "server"],
    "general": [],
}

COMPLEXITY_KEYWORDS: dict[str, list[str]] = {
    "high": ["complex", "large", "critical", "production", "migration", "security"],
    "medium": ["moderate", "update", "change", "improve"],
}


def _word_boundary(kw: str) -> str:
    escaped = re.escape(kw)
    if " " in kw:
        return escaped
    return rf"\b{escaped}\b"


def classify_task(task_context: str) -> str:
    context_lower = task_context.lower()
    for task_type, keywords in TASK_TYPES.items():
        for kw in keywords:
            if re.search(_word_boundary(kw), context_lower):
                return task_type
    return "general"


def estimate_complexity(task_context: str) -> str:
    context_lower = task_context.lower()
    for level, keywords in COMPLEXITY_KEYWORDS.items():
        for kw in keywords:
            if re.search(_word_boundary(kw), context_lower):
                return level
    return "low"


def make_analyze_task(registry: SkillRegistry):
    matcher = SkillMatcher(registry)

    def analyze_task(task_context: str, goal: str = "") -> dict:
        """Essential first step for ANY task. Analyzes the task, classifies it, and returns
        relevant skill recommendations and a suggested approach. Call this BEFORE starting
        any implementation, debugging, review, or planning work.

        Args:
            task_context: Describe what you're working on — the problem, code area, or feature.
            goal: Optional. What you want to achieve (e.g. "fix the bug", "implement feature X").

        Returns:
            Task analysis with type, complexity, recommended skills, and suggested approach.
        """
        task_type = classify_task(task_context)
        complexity = estimate_complexity(task_context)
        matched = matcher.find_relevant(f"{task_context} {goal}", top_k=5)

        if not matched:
            matched = matcher.find_relevant(task_type, top_k=3)

        approach = _build_approach(task_type, complexity, goal, matched)

        return TaskAnalysis(
            task_type=task_type,
            complexity=complexity,
            recommended_skills=matched,
            suggested_approach=approach,
        ).model_dump()

    return analyze_task


def _build_approach(
    task_type: str,
    complexity: str,
    goal: str,
    skills: list[MatchedSkill],
) -> str:
    parts = [f"Task classified as: {task_type} ({complexity} complexity)"]
    if goal:
        parts.append(f"Goal: {goal}")
    if skills:
        skill_names = ", ".join(s.name for s in skills)
        parts.append(f"Recommended skills: {skill_names}")
        parts.append("Use get_skill('<name>') to load full guidance for any recommended skill.")
    return "\n".join(parts)
