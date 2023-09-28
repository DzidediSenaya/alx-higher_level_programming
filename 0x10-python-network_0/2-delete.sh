#!/bin/bash
# This script takes a URL as an argument, sends a DELETE request to the URL using curl,
# and displays the body of the response.

# Check if a URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url="$1"

# Use curl to send a DELETE request and display the body of the response
curl -sX DELETE "$url"
