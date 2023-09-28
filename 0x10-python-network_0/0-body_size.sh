#!/bin/bash
# Takes a URL as an argument, sends a request to the URL using curl, and displays the size of the body of the response in bytes.
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}' | xargs -I {} echo {} bytes
