#!/bin/bash

SRC="/Users/nagasaisrinivasmaridu/Desktop/combined"
DEST="/Users/nagasaisrinivasmaridu/Desktop/ProjectFiles"

mkdir -p "$DEST"

# Copy only files, rename them using relative path (replace / with _)
find "$SRC" -type f | while read -r filepath; do
    relpath="${filepath#$SRC/}"             # Get relative path
    newname="${relpath//\//_}"              # Replace slashes with underscores
    cp "$filepath" "$DEST/$newname"
done
