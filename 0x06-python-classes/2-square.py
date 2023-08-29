#!/usr/bin/python3
"""Define the class Square"""


class Square:
    """Represent the square"""

    def __init__(self, size=0):
        """Describes the qualities of the Square

        Args:
            self (int): size of the square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
