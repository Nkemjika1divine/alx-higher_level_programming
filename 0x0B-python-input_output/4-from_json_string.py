#!/usr/bin/python3
"""Function that returns an object represented by json"""


def from_json_string(my_str):
    """Args:
    my_str: the string to switch to list/dictionary
    """
    return json.loads(my_str)
