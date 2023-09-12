#!/usr/bin/python3
"""Function that writes object to text file using json"""
import json


def save_to_json_file(my_obj, filename):
    """Args:
    my_obj: the object to write
    filename: the file to be written into
    """
    with open(filename, "w") as files:
        json.dump(my_obj, files)
