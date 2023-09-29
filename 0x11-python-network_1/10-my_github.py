#!/usr/bin/python3
"""
This script takes your GitHub username and personal access token
as arguments, uses Basic Authentication with the token to access
your GitHub information, and displays your GitHub user ID.
"""


import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        data = response.json()
        print(data.get("id"))
    else:
        print(None)
