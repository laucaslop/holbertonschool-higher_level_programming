#!/usr/bin/python3
""" Rectangle class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Initial """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Returns the area """
        return self.__height * self.__width

    def __str__(self):
        """ Returns the printable string """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
