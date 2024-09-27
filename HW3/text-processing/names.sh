#!/bin/bash

file=yellow_pages.csv

cat $file |egrep "^([^,]*,){1,}[^,]*$"| cut -d "," -f 1,2 | tr ',' ' ' | cut -d " " -f 1,2 | sort -k 2
