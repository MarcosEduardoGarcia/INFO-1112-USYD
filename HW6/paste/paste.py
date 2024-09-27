# YOUR CODE HERE
import sys
import os

no_file = len(sys.argv)

lines = []
len_file = []

for i in range(1, no_file):
    file = sys.argv[i]
    if os.path.exists(file):
        f = open(file,'r')
        content = f.readlines()

        for j in range(len(content)):
            content[j] = content[j].strip("\n")
        lines = lines + [content]
        len_file.append(len(content))
    else:
        print("Unable to load file", file)
        exit()

max_len = max(len_file)

for i in range(max_len):
    for j in range(len(lines)):
        if i < len_file[j]:
            if j == len(lines)-1:
                print(lines[j][i],end="")
            else:
                print(lines[j][i]+"\t",end="")
        else:
            if j == len(lines)-1:
                print("", end="")
            else:
                print("\t", end="")
    print("")