#!/usr/bin/python3
"""This function writes a string to a text file (UTF8) and returns the number of characters written"""


def write_file(filename="", text=""):
    """The function that does it"""
    with open(filename, "w", encoding="utf-8") as files:
        return files.write(text)
