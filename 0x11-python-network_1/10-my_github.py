#!/usr/bin/python3
"""Uses the GitHub API to display user id using Basic Authentication."""

import requests
import sys


def main():
    """Main function to fetch user id using GitHub API."""
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        print(response.json().get('id'))
    else:
        print("None")


if __name__ == "__main__":
    main()
