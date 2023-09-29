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
    email = sys.argv[2]

    payload = {'email': email}
    response = requests.post(url, data=payload)

    print("Your email is:", email)
    print(response.text)
