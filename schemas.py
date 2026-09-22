from pydantic import BaseModel

class RepoResponse(BaseModel):
    name : str
    full_name : str
    description : str | None
    language: str | None
    topics: list[str]
    stargazers_count: int | None
    forks_count : int | None
    open_issues_count : int
    default_branch : str

class RepoStatsResponse(BaseModel):
    name: str
    stars: int
    forks: int
    open_issues: int
    language: str | None