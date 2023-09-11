#!/usr/bin/python3
"""Defines a MyList class that inherits list"""


class MyList(list):
    """Sorted printing of a list"""

    def print_sorted(self):
        "Prints in sorted ascending orde"""
        print(sorted(self))
