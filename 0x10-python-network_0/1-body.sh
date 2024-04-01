#!/usr/bin/bash
# This script takes in a URL, sends a request to that URL, and displays the body of the response
curl -s -o /dev/null -w "%{http_code}" "$URL" | grep -q "200" && curl -s "$1"
