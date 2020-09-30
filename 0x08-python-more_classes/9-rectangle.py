#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """Area"""

        return self.__height * self.__width

    def perimeter(self):
        """Perimeter"""

        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):

        var = ''
        if self.__width is 0 or self.__height is 0:
            return var
        for i in range(self.__height):
            for j in range(self.__width):
                var += str(self.print_symbol)
            if i != self.__height - 1:
                var += '\n'
        return var

    def __repr__(self):
        """Rectangle's value"""

        w = str(self.__width)
        h = str(self.__height)
        var = "Rectangle(" + w + ", " + h + ")"
        return var

    def __del__(self):
        """Print bye rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare two rectangles"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """New rectangle instance"""

        height = size
        width = size

        return cls(height, width)
