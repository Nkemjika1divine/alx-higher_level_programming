#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = len(argv) - 1
    a = 0
    for i in range(count):
        a = a + int(argv[i + 1])
    print(f"{a:d}")
