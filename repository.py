from models import Repo
from sqlalchemy import select

class RepoRepository:

    def __init__(self, session):
        self.session = session

    def save(self, data):
        repo = Repo(
            name = data['name'],
            owner = data['owner']['login'],
            full_name	= data['full_name'],
            description	= data['description'],
            language = data['language'],
            topics = ','.join(data['topics']),
            stars = data['stargazers_count'],
            forks = data['forks_count'],
            open_issues	= data['open_issues_count'],
            default_branch	= data['default_branch'],
        )
        self.session.add(repo)
        self.session.commit()
        return repo

    def update(self, repo, data):
            repo.full_name = data["full_name"]
            repo.description = data["description"]
            repo.language = data["language"]
            repo.topics = ",".join(data["topics"])
            repo.stars = data["stargazers_count"]
            repo.forks = data["forks_count"]
            repo.open_issues = data["open_issues_count"]
            repo.default_branch = data["default_branch"]
            self.session.commit()
            return repo

    def get_by_owner_and_name(self, owner, name):
        statement = select(Repo).where(Repo.name == name, Repo.owner == owner)
        result = self.session.execute(statement).scalar_one_or_none()
        return result