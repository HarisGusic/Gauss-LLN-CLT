#!/usr/bin/env bash

td='/tmp/split_file_saf0u04$(%$KJ#IU#$5934'
destdir="$2"
name="$(basename "$1")"

mkdir -p "$td"
cp "$name" "$td/"

# Duplicate source file path

let i=1
while :; do
    pushd "$td" >/dev/null
    csplit -sf "${name}-" -n 1 "$name" '/##/' 2>/dev/null || break
    mv "${name}-0" "${name}_$i"
    tail -n +2 "${name}-1" > .tmpfile && mv .tmpfile "$name"
    popd >/dev/null
    cp "$td/${name}_$i" "$destdir/${name}_$i"
    let i++
done

popd 2>/dev/null 1>/dev/null
cp "$td/$name" "$destdir/${name}_$i"

rm -rf "$td/"
