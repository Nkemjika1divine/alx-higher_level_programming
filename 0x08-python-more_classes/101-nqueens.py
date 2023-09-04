#!/usr/bin/python3
"""Solves the N-queen game ouzzle"""


import sys

def 

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: nqueens N\n")
        sys.exit(1)

    if sys.argv[1].isdigit() is False:
        sys.stderr.write("N must be a number\n")
        sys.exit(1)

    if int(sys.argv[1]) < 4:
        sys.stderr.write("N must be at least 4\n")
        sys.exit(1)

    n = int(sys.argv[1])
    board = [[0 for i in range(n)] for i in range(n)]

    for row in board:
