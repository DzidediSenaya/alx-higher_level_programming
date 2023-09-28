#!/bin/bash
# Sends a JSON POST request to the URL passed as the first argument with the contents of the file
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
