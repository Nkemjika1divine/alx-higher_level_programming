#!/usr/bin/python3
"""This function reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """the function that does it"""
    with open(filename, "r", encoding="utf-8") as files:
        print(files.read(), end="")
