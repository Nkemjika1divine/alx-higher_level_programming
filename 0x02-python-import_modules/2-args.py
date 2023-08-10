#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = len(argv) - 1
    if count == 0:
        print(f"{count:d} arguments.")
    elif count == 1:
        print(f"{count:d} argument:")
    else:
        print(f"{count:d} arguments:")
    for i in range(count):
        print(f"{i + 1:d}: {argv[i + 1]}")
