#!/usr/bin/python3
""" Module """


def number_of_lines(filename=""):
    """Read a file"""

    number_of_lines = 0
    with open(filename, encoding="utf-8") as a_file:
        for _ in a_file:
            number_of_lines += 1
    return number_of_lines
