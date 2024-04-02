#!/usr/bin/python3
"""Sends a POST request with an email parameter and response body."""

import urllib.parse
import urllib.request
import sys


def main():
    """Main function to send a POST request with email parameter."""
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))


if __name__ == "__main__":
    main()
