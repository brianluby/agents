#!/bin/bash
# Simple agent conversion script

if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <input_file> <output_file> <claude|opencode>"
    exit 1
fi

INPUT="$1"
OUTPUT="$2"
FORMAT="$3"

if [ ! -f "$INPUT" ]; then
    echo "Error: Input file $INPUT not found"
    exit 1
fi

# Create output directory if needed
mkdir -p "$(dirname "$OUTPUT")"

if [ "$FORMAT" = "opencode" ]; then
    echo "Converting to OpenCode format..."

    # Extract content between --- markers
    awk '
    BEGIN { fm=0; }
    /^---$/ { fm++; if (fm==2) { getline; } next; }
    fm==1 {
        # Convert model names
        if ($1 == "model:") {
            if ($2 == "haiku") print "model: zai/glm-4.6";
            else if ($2 == "sonnet" || $2 == "opus") print "model: zai/glm-4.6";
            else print $0;
        }
        # Skip name and tags fields
        else if ($1 != "name:" && $1 != "tags:") {
            print $0;
        }
        # Add OpenCode specific fields
        if ($1 == "description:") {
            print "mode: subagent";
            print "temperature: 0.7";
        }
    }
    fm==0 || fm==2 { print $0; }
    ' "$INPUT" > "$OUTPUT"

    echo "Converted to OpenCode format: $OUTPUT"

elif [ "$FORMAT" = "claude" ]; then
    echo "Converting to Claude Code format..."

    # Extract filename without extension for name field
    NAME=$(basename "$OUTPUT" .md)

    # Convert the file
    awk -v name="$NAME" '
    BEGIN { fm=0; printed_name=0; }
    /^---$/ {
        fm++;
        print $0;
        if (fm==1 && !printed_name) {
            print "name: " name;
            printed_name=1;
        }
        next;
    }
    fm==1 {
        # Convert model names
        if ($1 == "model:") {
            if (index($0, "gpt-4.1-mini") > 0 || index($0, "haiku") > 0) print "model: haiku";
            else if (index($0, "gpt-5.1") > 0 || index($0, "sonnet") > 0 || index($0, "opus") > 0) print "model: sonnet";
            else print $0;
        }
        # Skip OpenCode specific fields
        else if ($1 != "mode:" && $1 != "temperature:" && $1 != "tools:" && $1 != "permissions:") {
            print $0;
        }
    }
    fm==0 || fm==2 { print $0; }
    ' "$INPUT" > "$OUTPUT"

    echo "Converted to Claude Code format: $OUTPUT"
else
    echo "Error: Format must be 'claude' or 'opencode'"
    exit 1
fi