#!/usr/bin/python3
""" Object from a JSON file """
import json


def load_from_json_file(filename):
    """ Creates an Object from a JSON """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.loads(file.read())
