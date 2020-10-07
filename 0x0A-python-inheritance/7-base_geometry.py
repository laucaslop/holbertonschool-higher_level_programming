#!/usr/bin/python3
""" Write BaseGeometry class """


class BaseGeometry():
    """ Defines the attributes of Geometric Shapes """

    def area(self):
        """ Defines the area """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Recieves the value property """

        if type(value) is not int:
            raise TypeError(name + " <name> must be an integer")
        if value <= 0:
            raise ValueError(name + " <name> must be greater than 0")
