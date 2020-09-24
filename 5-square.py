#!/usr/bin/python3
"""Creates a class Square"""


class Square:
        """Initialization of the class"""
        def __init__(self, size=0):
                self.__size = size

        def area(self):
                """Area"""
                return self.__size ** 2

        @property
        def size(self):
                """Size"""
                return self.__size

        @size.setter
        def size(self, value):
                """Set the size"""
                if type(value) is not int:
                        raise TypeError("size must be an integer")
                if value < 0:
                        raise ValueError("size must be >= 0")
                self.__size = value

        def my_print(self):
                """Print the square class"""
                if self.__size > 0:
                        for i in range(self.__size):
                                print("#" * self.__size)
                else:
                        print()
