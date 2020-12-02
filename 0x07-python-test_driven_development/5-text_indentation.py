#!/usr/bin/python3
""" This module defines the text_indentation function """


def text_indentation(text):
    """ Function that prints a text
    Arg: text """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""
    for i in text:
        if i == '\n':
            print("{}".format(new_text))
            new_text = ""
            continue
        else:
            new_text += i

        if i == '.' or i == '?' or i == ':':
            new_text = new_text.strip(" ")
            print("{}".format(new_text), end="")
            print("\n")
            new_text = ""

    new_text = new_text.strip(" ")
    print("{}".format(new_text), end="")
