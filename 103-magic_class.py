#!/usr/bin/python3
"""bytecode to python code"""
import math


class MagicClass:
    """Constructor"""

    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    """Calculates the area"""

    def area(self):
        return ((self.__radius ** 2) * math.pi)

    """Calculates the perimeter"""

    def circumference(self):
        return (2 * math.pi * self.__radius)
