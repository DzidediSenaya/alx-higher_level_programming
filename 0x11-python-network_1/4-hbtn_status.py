#!/usr/bin/python3
"""
This script fetches the status from https://alx-intranet.hbtn.io/status
and displays information about the response body using the requests package.
"""


import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    response = requests.get(url)
    body = response.text

    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
