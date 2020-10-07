#!/usr/bin/python3
"""" attr Module """


def add_attribute(obj, name, value):
    """ New attribute to an object if its possible """
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
