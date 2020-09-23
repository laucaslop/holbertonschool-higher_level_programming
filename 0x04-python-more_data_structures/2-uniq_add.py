#!/usr/bin/python3
def uniq_add(my_list=[]):
    n = set(my_list)
    m = 0
    for idx in n:
        m += idx
    return m
