#!/usr/bin/python3
"""
This script lists 10 commits (from the most recent to oldest)
of a repository by a specific user using the GitHub API.
"""


import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    base_url = "https://api.github.com/repos"
    url = f"{base_url}/{owner_name}/{repository_name}/commits"

    try:
        response = requests.get(url)
        commits = response.json()

        if response.status_code != 200:
            sys.exit(1)

        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")

    except Exception as e:
        print(e)
