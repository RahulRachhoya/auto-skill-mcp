from pathlib import Path

import yaml

from auto_skill_mcp.models import Skill

SKILL_DATA_DIR = Path(__file__).resolve().parent.parent / "skill_data"


class SkillRegistry:
    _skills: dict[str, Skill] = {}

    def __init__(self, skill_dir: Path | None = None) -> None:
        self.skill_dir = skill_dir or SKILL_DATA_DIR
        self._skills = {}
        self._load_all()

    def _load_all(self) -> None:
        if not self.skill_dir.exists():
            return
        for skill_path in self.skill_dir.iterdir():
            if not skill_path.is_dir():
                continue
            skill_file = skill_path / "SKILL.md"
            if not skill_file.exists():
                continue
            skill = self._parse_skill(skill_file)
            if skill:
                self._skills[skill.name] = skill

    def _parse_skill(self, path: Path) -> Skill | None:
        content = path.read_text(encoding="utf-8")
        parts = content.split("---", 2)
        if len(parts) < 3:
            return None
        try:
            frontmatter = yaml.safe_load(parts[1])
        except yaml.YAMLError:
            return None
        if not isinstance(frontmatter, dict):
            return None
        name = frontmatter.get("name", path.parent.name)
        description = frontmatter.get("description", "")
        metadata = frontmatter.get("metadata", {}) or {}
        return Skill(
            name=name,
            description=description,
            category=metadata.get("category", "uncategorized"),
            tags=metadata.get("tags", []),
            body=parts[2].strip(),
            file_path=str(path),
        )

    def get_all(self) -> list[Skill]:
        return list(self._skills.values())

    def get(self, name: str) -> Skill | None:
        return self._skills.get(name)

    def count(self) -> int:
        return len(self._skills)
