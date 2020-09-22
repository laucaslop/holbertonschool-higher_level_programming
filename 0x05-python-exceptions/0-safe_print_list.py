#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    p = 0
    while (p < x):
        try:
            print("{}".format(my_list[p]), end='')
        except IndexError:
            print()
            return p
        p += 1
    print()
    return p
