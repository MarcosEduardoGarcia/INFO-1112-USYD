#!/bin/bash

file=$1

# GET THE PERMISSIONS
perms=$(stat -c%a $file)
new=0$perms

name=$(ls -l $file | awk '{print $9}')
permissions=$(ls -l $file | awk '{print $1}')

echo $name 'had permissions:' $permissions '('$perms')'


final=$(printf "0%o" $(($new ^ 077))) 

chmod $final $file

perms=$(stat -c%a $file)
permissions=$(ls -l $file | awk '{print $1}')

echo $name 'now has permissions:' $permissions '('$perms')'
