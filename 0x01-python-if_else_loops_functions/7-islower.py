#!/usr/bin/python3
def islower(c):
    # ord() is used to check ascii values of letters
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
