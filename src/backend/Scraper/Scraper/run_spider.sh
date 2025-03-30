#!/bin/bash

# Check if at least two arguments are provided
if [ "$#" -lt 2 ]; then
    echo "Usage: $0 spider_name url1 [url2 url3 ...]"
    exit 1
fi

# Extract the spider name (first argument)
SPIDER_NAME="$1"
shift  # Shift arguments so that only URLs remain

# Convert the list of URLs into a JSON array
URLS_JSON=$(printf '%s\n' "$@" | jq -R . | jq -s .)

# Run Scrapy with the URLs as an argument
cd /Users/vidpesko/Documents/Learning/Projects/TerminiAlert/src/backend/Scraper/Scraper
scrapy crawl "$SPIDER_NAME" -a urls="$URLS_JSON"
