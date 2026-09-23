import requests

class RepositoryNotFoundError(Exception):
    pass

class GithubAPIError(Exception):
    pass

class RepositoryService:
    def __init__(self, github_client, repo_repository):
        self.github_client = github_client
        self.repo_repository = repo_repository

    def get_repository(self, owner, repo):
        try:
            data = self.github_client.get_repo(owner,repo)
            data_owner = data['owner']['login']
            data_name = data['name']
            data_exist = self.repo_repository.get_by_owner_and_name(data_owner, data_name)
            if data_exist: 
                self.repo_repository.update(data_exist, data)
            else:
                self.repo_repository.save(data)

            return data
        
        except requests.exceptions.HTTPError as errh:
            if(errh.response.status_code ==404):
                raise RepositoryNotFoundError("Repository Not found")
            else:
                raise GithubAPIError("Github API Error")
        except requests.exceptions.RequestException:
            raise GithubAPIError("Github API Error")
