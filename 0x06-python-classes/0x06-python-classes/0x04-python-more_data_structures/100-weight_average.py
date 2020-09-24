#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        mul = 0
        add = 0
        for item in my_list:
            mul += item[0] * item[1]
            add += item[1]
        average = mul / add
    return average
