#!/usr/bin/python3
"""Define the class square"""


class Square:
    """Represent the class square"""

    def __init__(self, size=0):
        """Initializing the init method

        Args:
            size (int): the size of the square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Return area of the square"""

        c = self.__size * self.__size
        return (c)
