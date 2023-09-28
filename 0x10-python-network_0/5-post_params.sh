#!/bin/bash
# This script takes a URL as an argument, sends a POST request to the URL using curl
# with specific parameters (email and subject), and displays the body of the response.

# Check if a URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url="$1"

# Define the email and subject variables
email="test@gmail.com"
subject="I will always be here for PLD"

# Use curl to send a POST request with specific parameters and display the body of the response
curl -sX POST -d "email=$email" -d "subject=$subject" "$url"
