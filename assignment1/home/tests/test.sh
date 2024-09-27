#!/bin/bash

# Defining the dates of files
touch -a -m -t 201512180145 test1/file1.ext
chmod 777 test1/file1.ext 
touch -a -m -t 201905220945 test1/file2.ext
chmod 666 test1/file2.ext
touch -a -m -t 200104071010 test1/file3.ext
chmod 715 test1/file3.ext
touch -a -m -t 202106160205 test1/folder/file4.ext
chmod 634 test1/folder/file4.ext
echo ======================================================
echo -e "Showing permissions before use python program:\n "

ls -l test1/file*.ext
ls -l test1/folder/f*
echo ======================================================
#Running code 
echo -e "Running python code"
python3 pcontrol.py

echo "In pcontrol.py I can use main function as many times as I need i this case I use twice main(input, output) function (lines 96 and 97) to run 2"
echo "tests at the same time reading filelist1txt, and filelist_not_existent "
echo "and creating the corresponding outputs output1 and output2 inside corresponding folder test1 and test2. " 

echo -e "\n"
echo ======================================================
echo -e "Permissions after execute code, the group execute permissions has been toggled: \n"
ls -l test1/file*.ext
ls -l test1/folder/f*
echo ======================================================
echo -e "Using diff to compare exp_output and output1: \n"

diff -s test1/output1.txt test1/exp_output.txt

echo -e "\nUsing diff to compare exp_output2 and output2: \n "

diff -s test2/output2.txt test2/exp_output2.txt

echo ======================================================
echo -e "\n"


