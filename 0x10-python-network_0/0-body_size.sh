#!/bin/bash
# Takes a URL as an argument, sends a request to that URL using curl, and displays the size of the response body in bytes.
curl -s "$1" | wc -c
