#!/bin/bash
# Takes a URL as an argument, sends a GET request to the URL using curl, and displays the body of the response if the response status code is 200.
curl -sL "$1"
