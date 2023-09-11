#!/usr/bin/python3
"""A class checking function"""


def is_same_class(obj, a_class):
    """Checks if an objecr i an instance of a class"""

    if type(obj) == a_class:
        return True
    return False
