#!/usr/bin/bash
URL=$1
curl -sI "$URL" | grep -i Content-Length | awk '{print $2}'
