#!/bin/bash
# This script takes a URL as an argument, sends a GET request to the URL using curl
# with a custom header X-School-User-Id: 98, and displays the body of the response.

# Check if a URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url="$1"

# Use curl to send a GET request with a custom header and display the body of the response
curl -sH "X-School-User-Id: 98" "$url"
