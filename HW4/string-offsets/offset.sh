#!/bin/bash

chmod +x $1
output=$(./$1)

if [ $2 == 'o' ]
then
    result=$(strings -t o $1 | grep "$output" | awk '{print $1}')
    echo Offset of string: \"$output\" is $result in octal.
elif [ $2 == 'x' ]
then
    result=$(strings -t x $1 | grep "$output" | awk '{print $1}')
    echo Offset of string: \"$output\" is $result in hexadecimal.
elif [ $2 == 'd' ]
then
    result=$(strings -t d $1 | grep "$output" | awk '{print $1}')
    echo Offset of string: \"$output\" is $result in decimal.
fi




