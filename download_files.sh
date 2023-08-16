#!/bin/bash

# Read each line from the input file
while IFS=$'\t' read -r file_name url; do
    # Skip header row
    if [[ "$file_name" != "file_name" && "$url" != "cdn_link" ]]; then
        # Download the file using curl
        echo "Downloading $file_name from $url"
        curl -o "$file_name" "$url"
        echo "Download of $file_name complete"
    fi
done < input.txt
