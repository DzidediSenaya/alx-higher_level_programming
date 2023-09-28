#!/bin/bash
# This script sends a request to a URL passed as an argument and displays only the status code of the response.

# Check if a URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url="$1"

# Use curl to send a request and format the output to display only the status code
status_code=$(curl -s -o /dev/null -w "%{http_code}" "$url")
echo "$status_code"`
