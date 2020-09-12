#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max = my_list[0]
        for numb in my_list:
            if numb > max:
                max = numb
        return max
    return None
