#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo_name}/commits"
    response = requests.get(url)
    commits = response.json()
    for commit in commits[:10]:
        print(f"{commit.get('sha')}: {commit.get('commit').get('author').get('name')}")
