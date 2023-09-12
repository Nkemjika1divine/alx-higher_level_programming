#!/usr/bin/python3
"""This function appends a string at the end of a text file and returns the number of characters added"""


def append_write(filename="", text=""):
    """the function that does it"""
    with open(filename, "a", encoding="utf-8") as files:
        return files.write(text)
