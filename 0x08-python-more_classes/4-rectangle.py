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
        """Getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter"""
        self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """Getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter"""
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

    def __str__(self):
        var = ''
        if self.__width is 0 or self.__height is 0:
            return var
        for i in range(self.__height):
            if i == self.__height - 1:
                var += '#' * self.__width
            else:
                var += '#' * self.__width + '\n'
        return var

    def __repr__(self):
        """Rectangle's value"""

        w = str(self.__width)
        h = str(self.__height)
        var = "Rectangle(" + w + ", " + h + ")"
        return var
