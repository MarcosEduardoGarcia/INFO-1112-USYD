#!/bin/bash

cat employees.txt | head -n 1 > employees_updated.txt
cat employees.txt | awk -F "," '$1 >= 100 ' | tail -n +2 | awk -F "," '{$5+=5000;}1' OFS=, >> employees_updated.txt
cat employees.txt | awk -F "," '$1 < 100 ' >> employees_updated.txt 

sort -t"," -k1n,1 employees_updated.txt -o employees_updated.txt

