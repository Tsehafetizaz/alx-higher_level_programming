#!/usr/bin/python3
"""Displays the body of the response or error code  using requests."""

import requests
import sys


def main():
    """Main function to retrieve and display response body or error code."""
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)


if __name__ == "__main__":
    main()
