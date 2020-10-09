#!/usr/bin/python3
""" Module """
import json


def save_to_json_file(my_obj, filename):
    """ Save Object to a file """
    with open(filename, "w") as write_file:
        json.dump(my_obj, write_file)
