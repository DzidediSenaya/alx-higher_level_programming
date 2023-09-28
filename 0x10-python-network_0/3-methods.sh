#!/bin/bash
# This script takes a URL as an argument and displays all HTTP methods the server will accept.

# Check if a URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url="$1"

# Use curl with the -i (include headers) option to send an OPTIONS request and retrieve the server's allowed methods
allowed_methods=$(curl -sI "$url" | grep "Allow" | sed 's/Allow: //')

# Check if the Allow header exists
if [ -z "$allowed_methods" ]; then
    echo "Error: Allow header not found in the response."
    exit 1
fi

echo "$allowed_methods"
