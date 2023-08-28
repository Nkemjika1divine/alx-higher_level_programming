#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        a = fct(*args)
        return (a)
    except:
        print("Exception: {}".format(sys.exc_info()[1], file=sys.stderr))
        return (None)

