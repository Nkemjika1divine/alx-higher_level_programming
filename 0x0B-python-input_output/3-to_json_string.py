#!/usr/bin/python3
"""Function that returns the json representation of an object"""


def to_json_string(my_obj):
    """Args:
    my_obj: the list/dictionary to return its representation
    """
    return json.dumps(my_obj)
