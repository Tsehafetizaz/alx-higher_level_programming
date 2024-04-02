#!/usr/bin/python3
"""Uses GitHub API to list recent commits of a repository by a user."""

import requests
import sys


def main():
    """Main function to fetch and display recent commits of a repository."""
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)
    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:
            sha = commit.get('sha')
            author = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author}")
    else:
        print("Error fetching commits.")


if __name__ == "__main__":
    main()
