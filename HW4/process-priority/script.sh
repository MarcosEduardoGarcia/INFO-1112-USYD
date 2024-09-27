#!/bin/bash

renice -n $2 -p $(ps -eo comm,pid | grep ^$1 | awk '{print $2}')