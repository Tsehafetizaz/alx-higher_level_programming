#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status using urllib."""

import urllib.request

def main():
    """Main function to fetch and display status."""
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        content = response.read()
        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", content.decode('utf-8'))

if __name__ == "__main__":
    main()
