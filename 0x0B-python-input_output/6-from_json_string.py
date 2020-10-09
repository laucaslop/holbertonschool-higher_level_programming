#!/usr/bin/python3
""" from JSON to string """
import json


def from_json_string(my_str):
    """ Returns an object by a JSON representation """
    return json.loads(my_str)
