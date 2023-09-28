#!/bin/bash
# Takes a URL as an argument, sends a request to the URL using curl, and displays only the status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
