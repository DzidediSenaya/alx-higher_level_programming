#!/bin/bash
# This script sends a JSON POST request to a URL with the contents of a file
# and displays the body of the response.

# Check if two arguments (URL and JSON file) are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <URL> <JSON file>"
    exit 1
fi

# Get the URL and JSON file from the command line arguments
url="$1"
json_file="$2"

# Check if the JSON file exists
if [ ! -f "$json_file" ]; then
    echo "Error: JSON file '$json_file' not found."
    exit 1
fi

# Use curl to send a JSON POST request with the contents of the file and display the body of the response
response=$(curl -s -H "Content-Type: application/json" -X POST -d @"$json_file" "$url")

# Check if the response contains "Valid JSON"
if [[ "$response" == *"Valid JSON"* ]]; then
    echo "Valid JSON"
else
    echo "Not a valid JSON"
fi
