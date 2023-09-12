#!/usr/bin/python3
"""function appends a string at the end of a file, returns no of chars app."""


def append_write(filename="", text=""):
    """the function that does it"""
    with open(filename, "a", encoding="utf-8") as files:
        return files.write(text)
