from typing import Any

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from auto_skill_mcp.models import MatchedSkill
from auto_skill_mcp.skills.registry import SkillRegistry


class SkillMatcher:
    def __init__(self, registry: SkillRegistry) -> None:
        self.registry = registry
        self._vectorizer: TfidfVectorizer | None = None
        self._tfidf_matrix: Any = None
        self._skill_names: list[str] = []
        self._build_index()

    def _build_index(self) -> None:
        skills = self.registry.get_all()
        if not skills:
            self._vectorizer = None
            self._tfidf_matrix = None
            self._skill_names = []
            return

        self._skill_names = [s.name for s in skills]
        # Field-weighted indexing: name(3x), description(2x), tags(2x), body(1x)
        docs = []
        for s in skills:
            name_part = " ".join(s.name.replace("-", " ").split()) + " "
            desc_part = s.description
            tags_part = " ".join(s.tags)
            body_part = s.body
            docs.append(
                (name_part * 3) + " " + (desc_part * 2) + " " + (tags_part * 2) + " " + body_part
            )

        self._vectorizer = TfidfVectorizer(
            stop_words="english",
            max_features=5000,
            ngram_range=(1, 2),
        )
        self._tfidf_matrix = self._vectorizer.fit_transform(docs)

    def find_relevant(self, query: str, top_k: int = 5) -> list[MatchedSkill]:
        if self._vectorizer is None or self._tfidf_matrix is None:
            return []
        query_vec = self._vectorizer.transform([query])
        scores = cosine_similarity(query_vec, self._tfidf_matrix).flatten()
        top_indices = scores.argsort()[::-1][:top_k]
        results = []
        for idx in top_indices:
            score = float(scores[idx])
            if score <= 0:
                continue
            skill = self.registry.get(self._skill_names[idx])
            if skill is None:
                continue
            results.append(
                MatchedSkill(
                    name=skill.name,
                    description=skill.description,
                    category=skill.category,
                    score=round(score, 3),
                )
            )
        return results
