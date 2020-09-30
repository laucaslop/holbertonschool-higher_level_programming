#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """Getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    @property
    def width(self):
        """Getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        string = ""
        if self.__width != 0 or self.__height != 0:
            for row in range(self.__height):
                for _ in range(self.__width):
                    string += "#"
                if row < self.__height - 1:
                    string += "\n"
        return string

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
