#!/usr/bin/python3
""" Getz x-Request-ld """
from sys import argv
import requests


if __name__ == '__main__':
    print(requests.get(argv[1]).headers.get('x-Request-Id'))
