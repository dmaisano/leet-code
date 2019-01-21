#!/bin/bash

count=0
while read line && [ $count -le 10 ]; do
  let 'count = count + 1'
  if [ $count -eq 10 ]; then
    echo $line
    exit 0
  fi
done < file.txt

# file.txt example
# Line 1
# Line 2
# Line 3
# Line 4
# Line 5
# Line 6
# Line 7
# Line 8
# Line 9
# Line 10
