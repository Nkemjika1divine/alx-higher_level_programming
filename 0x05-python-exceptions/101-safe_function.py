#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        a = fct(*args)
        return (a)
    except (ValueError, TypeError):
        print("Exception: {}".format(sys.exc_info()[1], file=sys.stderr))
        return (None)
