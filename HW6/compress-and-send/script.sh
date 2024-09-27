#!/bin/bash

cat $1 | gzip > compres.gz

(echo SEND $1 && cat compres.gz) > data

./netcat 127.0.0.1 8787 < data