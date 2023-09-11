#!/usr/bin/python3
"""This is a BaseGeometry class"""


class BaseGeometry:
    """Setting up the class"""

    def area(self):
        """This raises an exceotion because it is not implemnted"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This validates the integer entered"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value < 1:
            raise ValueError("<name> must be greater than 0")
