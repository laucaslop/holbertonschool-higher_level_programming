#!/usr/bin/python3
""" Module """


def append_after(filename="", search_string="", new_string=""):
    """ Function """

    with open(filename, encoding="utf-8") as a_file:
        lines = a_file.readlines()
        for line in lines:
            if search_string in line:
                lines.insert(lines.index(line) + 1, new_string)
    new_line = "".join(lines)

    with open(filename, mode="w", encoding="utf-8") as a_file:
        a_file.write(new_line)
