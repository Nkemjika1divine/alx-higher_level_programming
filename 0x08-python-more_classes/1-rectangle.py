#!/usr/bin/python3
"""Defines the class Rectangle"""


class Rectangle:
    """Initializing the class"""

    def __init__(self, width=0, height=0):
        """Describing the init method

        Args:
            Width (int): the width of the rectangle
            Height (int): the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the value stored at self.widtg"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets the value at self.width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the value stored at self.height"""
        return (self.__height)

    @width.setter
    def height(self, value):
        """sets the value at self.height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
