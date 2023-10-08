#!/bin/bash

filePath="links"
content=$(<"$filePath")
if [ $? -ne 0 ]; then
    echo "Error reading the file: $filePath"
    exit 1
fi

while read -r link; do
    listOfLink+=("$link")
done <<< "$content"


cwd=$(pwd)
absoluteDir="$cwd/python"

if ! cd "$absoluteDir"; then
    echo "Error changing directory to: $absoluteDir"
    exit 1
fi

for link in "${listOfLink[@]}"
do
    IFS='/' read -r -a parts <<< "$link"
    if [ "${#parts[@]}" -gt 5 ]; then
        link="https://leetcode.com/problems/${parts[6]}/"
    fi
    bash ../scripts/workflow.sh $link .py
done