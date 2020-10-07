#!/usr/bin/python3
""" Square 1 """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square 1"""

    def __init__(self, size):
        """Initial"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2
