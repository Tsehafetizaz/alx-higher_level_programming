#!/usr/bin/python3
"""Sends a POST request with an email parameterponse body using requests."""

import requests
import sys


def main():
    """Main function to send a POST request with email parameter."""
    url = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url, data={'email': email})
    print(response.text)


if __name__ == "__main__":
    main()
