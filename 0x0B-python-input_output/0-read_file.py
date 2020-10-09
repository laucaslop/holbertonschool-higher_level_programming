#!/usr/bin/python3
""" Module """


def read_file(filename=""):
    """Read the file"""

    with open(filename, encoding="utf-8") as a_file:
        data = a_file.read()
    print(data, end="")
