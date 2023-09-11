#!/usr/bin/python3
"""This checks if an object belongs to a class that is inhrited"""


def inherits_from(obj, a_class):
    """The fujction that check the object"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
