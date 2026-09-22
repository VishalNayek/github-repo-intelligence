from fastapi import FastAPI, HTTPException
from schemas import RepoResponse, RepoStatsResponse
from github_client import GithubClient
from service import RepositoryService, RepositoryNotFoundError, GithubAPIError
api = FastAPI()

client = GithubClient()
service = RepositoryService(client)

@api.get("/")
def get_root():
    return {"message" : "Welcome to Github Repo Intelligence"}

@api.get("/repositories/{owner}/{repo}", response_model=RepoResponse)
def get_repo(owner : str, repo : str):
    try:
        data = service.get_repository(owner, repo)
        return data
    except RepositoryNotFoundError:
        raise HTTPException(status_code=404, detail="Repository does not exist.")
    except GithubAPIError:
        raise HTTPException(status_code=503, detail="Github API error.")

@api.get("/repositories/{owner}/{repo}/stats", response_model=RepoStatsResponse)
def get_repo_stats(owner : str, repo : str):
    try:
        data = service.get_repository(owner, repo)
        stats = {
            "name" : data['name'],
            "stars" : data['stargazers_count'],
            "forks" : data['forks_count'],
            "open_issues" : data['open_issues_count'],
            "language" : data['language']
        }
        return stats
    except RepositoryNotFoundError:
        raise HTTPException(status_code=404, detail="Repository does not exist.")
    except GithubAPIError:
        raise HTTPException(status_code=503, detail="Github API error.")
