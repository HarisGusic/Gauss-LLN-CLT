#!/usr/bin/env bash

# Usage: split-file input destination_directory

# Split the specified file input into multiple files input_1, input_2, ... The
# content of each file is delimited by lines starting with ### in the original
# file.

td='/tmp/split_file_saf0u04$(%$KJ#IU#$5934' # Temp. dir. for intermediate files
destdir="$2"
name="$(basename "$1")" # Input file name stripped of its path

# Create temporary directory
mkdir -p "$td"
cp "$name" "$td/"

# Split the file into subfiles

pushd "$td" >/dev/null # Go to temporary directory
csplit -sf "${name}_" -n 1 "$name" '/^###/' '{*}' 2>/dev/null
popd 2>/dev/null 1>/dev/null # Return to original directory

let i=1 # Counts the number of subfiles processed
for file in "$td/$name"_*; do
    # Do not include the lines containing ###
    # Additionally, replace č with c so LaTeX can compile
    # Then move the file to the destination directory
    sed -e '/^###/d' -e 's/č/c/g' "$file" > "$destdir/${name}_$i"
    let i++
done

rm -rf "$td/" # Delete the temporary directory
