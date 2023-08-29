#!/usr/bin/python3
"""Defining the class Square"""


class Square:
    "Initializatiom of fhe class"""

    def __init__(self, size=0):
        """Elements of the method

        Args:
            size (int): size of the square
        """
        self.size = size

    @property
    def size(self):
        """return the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of he square"""
        return (self.__size ^ 2)

    def my_print(self):
        """prints the square with the char #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print("")
