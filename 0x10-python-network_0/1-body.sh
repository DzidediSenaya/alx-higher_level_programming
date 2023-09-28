#!/bin/bash
# This script takes a URL as an argument, sends a GET request to the URL using curl,
# and displays the body of the response if the response status code is 200.

# Check if a URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url="$1"

# Use curl to send a GET request and store the response in a variable
response=$(curl -s -o /dev/stdout -w "%{http_code}" "$url")

# Extract the status code from the response
status_code=${response: -3}

# Check if the status code is 200 (OK)
if [ "$status_code" -eq 200 ]; then
    # Display the body of the response
    curl -s "$url"
else
    echo "Status code: $status_code"
fi
