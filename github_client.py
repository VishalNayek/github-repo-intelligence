import requests
from dotenv import load_dotenv
import os

class GithubClient:
    def __init__(self):
        load_dotenv()
        self.github_token = os.getenv("GITHUB_TOKEN")
        if self.github_token is None:
            raise RuntimeError("Github Token Missing")


    def get_repo(self, owner, repo):
        token = self.github_token
        request_headers = {"Authorization": f"Bearer {token}"}
        url = f"https://api.github.com/repos/{owner}/{repo}"
        try:
            response = requests.get(url, headers = request_headers, timeout=5)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException:
            raise