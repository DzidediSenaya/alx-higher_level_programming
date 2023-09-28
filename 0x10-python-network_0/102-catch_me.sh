#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with "You got me!".

# Use curl to make a request with a custom header "Origin: HolbertonSchool" to trigger the desired response
curl -sL -X PUT -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me -d "user_id=98"
