#!/usr/bin/python3
"""Displays the body of the response or error code if an HTTPError occurs."""

import urllib.error
import urllib.request
import sys


def main():
    """Main function to retrieve and display response body or error code."""
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)


if __name__ == "__main__":
    main()
