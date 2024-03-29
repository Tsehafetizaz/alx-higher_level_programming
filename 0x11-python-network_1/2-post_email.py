#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email)
    data = data.encode('ascii')
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
