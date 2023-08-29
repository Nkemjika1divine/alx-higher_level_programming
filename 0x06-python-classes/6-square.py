#!/usr/bin/python3
"""Defining the class Square"""


class Square:
    "Initializatiom of fhe class"""

    def __init__(self, size=0, position=(0, 0)):
        """Elements of the method

        Args:
            size (int): size of the square
            posiition (int, int): the position of new square
        """
        self.size = size
        self.position = position

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


    @property
    def position(self):
        """Return position ic new square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) and num > 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of he square"""
        return (self.__size ^ 2)

    def my_print(self):
        """prints the square with the char #"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
