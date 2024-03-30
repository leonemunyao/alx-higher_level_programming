#!/usr/bin/bash

# Get the URL from the command line argument
url=$1

# Send a request to the URL and store the response in a variable
response=$(curl -sI "$url")

# Extract the content length from the response headers
content_length=$(echo "$response" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r')

# Display the content length in bytes
echo "The size of the body of the response is $content_length bytes"
