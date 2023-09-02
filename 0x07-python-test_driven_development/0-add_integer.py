#!/usr/bin/python3
"""Defines an addition  function"""


def add_integer(a, b=98):
    """Returns the sum of the ints

    float values are typecasted to int before addition

    Raises:
        TypeError: if a or b isnt integers or floats
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
