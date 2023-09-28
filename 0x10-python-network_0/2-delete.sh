#!/bin/bash
# Sends a DELETE request to the URL passed as the first argument using curl
curl -s -X DELETE "$1"
