#!/usr/bin/python3
"""Displays the value of the X-Request-Id response header using requests."""

import requests
import sys


def main():
    """Main function to retrieve and display X-Request-Id."""
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))


if __name__ == "__main__":
    main()
