#!/usr/bin/bash
URL="$1"
curl -s -o /dev/null -w "%{http_code}" "$URL" | grep -q "200" && curl -s "$URL"
