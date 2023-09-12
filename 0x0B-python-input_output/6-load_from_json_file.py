#!/usr/bin/python3
"""Function that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """Args:
    filename: the file to create the object from
    """
    with open(filename, "r", encoding="utf-8") as files:
        return json.load(files)
