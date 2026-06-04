from pydantic import BaseModel


class Skill(BaseModel):
    name: str
    description: str
    category: str
    tags: list[str]
    body: str
    file_path: str


class MatchedSkill(BaseModel):
    name: str
    description: str
    category: str
    score: float


class TaskAnalysis(BaseModel):
    task_type: str
    complexity: str
    recommended_skills: list[MatchedSkill]
    suggested_approach: str
