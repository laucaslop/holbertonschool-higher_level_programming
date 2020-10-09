#!/usr/bin/python3
""" Module """


def append_write(filename="", text=""):
    """ Text file """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
