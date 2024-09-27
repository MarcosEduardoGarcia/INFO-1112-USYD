#!/bin/bash

echo Version: $(uname -v --kernel-version)
echo Kernel Name: $(uname -s --kernel-name)
echo Operating System: $(cat /etc/os-release| grep '^NAME'|cut -d "=" -f2 |tr -d '"')
echo CPU: $(cat /proc/cpuinfo | grep "model name" | head -1 | cut -d ":" -f2)
echo Total Memory: $(cat /proc/meminfo | grep "MemTotal" | cut -d ":" -f2)
echo Hostname: $(cat /proc/sys/kernel/hostname)
echo User: $USER
echo Hardware: $(uname -srm | cut -d " " -f3)
