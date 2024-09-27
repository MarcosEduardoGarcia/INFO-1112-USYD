#!/bin/bash

if [ $# -lt 1 ]
    then
    printf "Not enough arguments\n"
    exit 0
elif [ $# -gt 1 ]
    then
    printf "Too many arguments\n"
    exit 0
fi

path=$1

result=($(ls -p $path | grep -v / | wc -l)) 

echo $path 'has' $result 'files'

