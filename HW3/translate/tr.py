import sys

def listtoString(s):
    out = ""
    return out.join(s)


if len(sys.argv) == 1:
    print('No arguments')
    sys.exit(1)
elif len(sys.argv) < 3:
    print('Not enough arguments')
    sys.exit(1)
elif len(sys.argv) > 3:
    print('Too many arguments')
    sys.exit(1)

original = str(sys.argv[1])
original = list(original)

replace = str(sys.argv[2])
replace = list(replace)


while True:

    str_input = input()
    str_input = list(str_input)
    for i in range(len(str_input)):
        if str_input[i] in original:
            index = original.index(str_input[i])
            str_input[i] = replace[index]
        else:
            pass
    print(listtoString(str_input))
