#!/usr/bin/python3
"""Creates a class Square"""


class Square():
    """Sq class"""

    def __init__(self, size=0):
        """Size"""
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        """Area"""

        return self.__size ** 2
