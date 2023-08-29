#!/usr/bin/python3
"""Define th class Square"""


class Square:
    """Represebt the class square"""

    def __init__(self, size=0):
        """Initializing th square

        Args:
            size (int): the aize of th square
        """
        self.__size = size

    @property
    def size(self):
        """the current size of rhe square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Returns the area of the circle"""
        c = self.__size * self.__size
        return (c)
