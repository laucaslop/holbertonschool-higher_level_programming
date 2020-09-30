#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle():
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        return int(self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width) + 2 * (self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        string = ""
        for item in range(self.__height):
            string += str(self.print_symbol) * self.__width
            string += '\n'
        string = string[:-1]
        return string

    def __repr__(self):
        return self.print_symbol

    def __del__(self):
        """Delete"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
