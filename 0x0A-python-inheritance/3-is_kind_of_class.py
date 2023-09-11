#!/usr/bin/python3
"""this check for a class an inherite class"""


def is_kind_of_class(obj, a_class):
    """Checks if an object belongs to a class or inherited class"""
    if isinstance(obj, a_class):
        return True
    return False
