#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialize"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter function of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter function of width"""
        self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """Getter function of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function of height"""
        self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
