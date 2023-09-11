#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""
    def __init__(self, size):
        """Initialize a new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return area of the square"""
        return super().area()

    def __str__(self):
        """Return str() for the square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
