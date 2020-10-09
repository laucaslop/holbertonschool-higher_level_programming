#!/usr/bin/python3
""" Module """


class MyClass:
    """ Returns the dictionary description """

    def __init__(self, name):
        self.name = name
        self.number = 0

    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.name, self.number)
