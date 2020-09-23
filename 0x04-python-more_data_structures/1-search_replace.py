#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for m, item in enumerate(new_list):
        if item is search:
            new_list[m] = replace
    return new_list
