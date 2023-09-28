#!/bin/bash
# This script takes a URL as an argument, sends a request to that URL using curl,
# and displays the size of the response body in bytes.

# Check if a URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url="$1"

# Use curl with the -s (silent) and -I (head) options to fetch the HTTP header
# Then, grep the Content-Length header to extract the size in bytes
body_size=$(curl -sI "$url" | grep -i "Content-Length" | awk '{print $2}')

# Check if Content-Length header exists
if [ -z "$body_size" ]; then
    echo "Error: Content-Length header not found in the response."
    exit 1
fi

echo "$body_size"
