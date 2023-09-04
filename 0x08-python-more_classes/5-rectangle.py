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

    @height.setter
    def height(self, value):
        """sets the value at self.height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Calculates the perimeter of the rectangle"""
        if (self.__width == 0) or (self.__height == 0):
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """returns a reoresentatiok of the rectangle using #"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        return ("\n".join(["#" * self.__width] * self.__height))

    def __repr__(self):
        """returns string reoresetaion of rectangle"""
        r = "Rectangle(" + str(self.__width)
        r += ", " + str(self.__height) + ")"
        return (r)

    def __del__(self):
        """prints a message when an instance is deleted"""
        print("Bye rectangle...")
