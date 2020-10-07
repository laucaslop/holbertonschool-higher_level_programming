#!/usr/bin/python3
""" MyInt class """


class MyInt(int):
    """ MyInt class """

    def __ne__(self, next):
        """ Returns == check """
        return super().__eq__(next)

    def __eq__(self, next):
        """ Returns != check """
        return super().__ne__(next)
