#!/usr/bin/python3
"""
This script takes a URL and an email address as input, sends
a POST request to the URL with the email as a parameter, and
displays the body of the response using the requests package.
"""


import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)
