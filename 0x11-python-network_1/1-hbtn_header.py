#!/usr/bin/python3
"""
This script takes a URL as input, sends a request to the URL,
and displays the value of the X-Request-Id variable found in
the header of the response.
"""


import urllib.request
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader("X-Request-Id")
        if x_request_id is not None:
            print(x_request_id)
