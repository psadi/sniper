# -*- coding: utf-8 -*-


from typing import Dict


class ApiEndpoints:
    def __init__(self, owner_org: str, repo: str, token: str):
        self.github_host: str = "https://api.github.com"
        self.owner_org = owner_org
        self.repo = repo
        self.headers: dict = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
        }

    def get_org_repos(self) -> Dict:
        return {
            "url": f"{self.github_host}/orgs/{self.owner_org}/repos",
            "headers": self.headers,
        }

    def get_owner_repos(self) -> Dict:
        return {
            "url": f"{self.github_host}/users/{self.owner_org}/repos",
            "headers": self.headers,
        }

    def get_repository_content(self) -> Dict:
        return {
            "url": f"{self.github_host}/repos/{self.owner_org}/{self.repo}/contents",
            "headers": self.headers,
        }
