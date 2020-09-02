#!/usr/bin/python3
def uppercase(str):
    for a in str:
        upper = ord(a)
        if upper > 96 and upper < 123:
            upper = ord(a) - 32
        print("{}" .format(chr(upper)), end="")
    print("")
