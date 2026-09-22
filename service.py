from github_client import GithubClient
import requests

class RepositoryNotFoundError(Exception):
    pass

class GithubAPIError(Exception):
    pass

class RepositoryService:
    def __init__(self, github_client):
        self.github_client = github_client

    def get_repository(self, owner, repo):
        try:
            data = self.github_client.get_repo(owner,repo)
            return data
        except requests.exceptions.HTTPError as errh:
            if(errh.response.status_code ==404):
                raise RepositoryNotFoundError("Repository Not found")
            else:
                raise GithubAPIError("Github API Error")
        except requests.exceptions.RequestException:
            raise GithubAPIError("Github API Error")
