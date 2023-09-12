#!/usr/bin/python3
"""Function that returns the dictionary representation of objects."""


def class_to_json(obj):
    """Return the dictionary represntation of obj."""
    return obj.__dict__
