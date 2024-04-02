#!/usr/bin/python3
"""Displays the value of the X-Request-Id var the response."""

import urllib.request
import sys


def main():
    """Main function to retrieve and display X-Request-Id."""
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))


if __name__ == "__main__":
    main()
