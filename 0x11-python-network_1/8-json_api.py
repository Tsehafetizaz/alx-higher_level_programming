#!/usr/bin/python3
"""Sends a POST request with a letter parameter """

import requests
import sys


def main():
    """Main function to send a POST request with letter parameter."""
    if len(sys.argv) < 2:
        q = ''
    else:
        q = sys.argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data={'q': q})
    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response.get('id'),
                                   json_response.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
