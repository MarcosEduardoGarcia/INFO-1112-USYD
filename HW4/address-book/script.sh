#!/bin/bash

name=$2

grep "$name" $1 | awk -F "," '{print "Name: " $1",", "Email: " $3}'

#grep 'John Smith' book.csv | awk -F "," '{print "Name: " $1",", "Email: " $3}'