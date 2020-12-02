#!/usr/bin/python3
""" Add_integer returns the sum of two integers
c = a + b """


def add_integer(a, b=98):
    """ Add two integers
    Args:
    a: first
    b: second
    Return: a + b """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
