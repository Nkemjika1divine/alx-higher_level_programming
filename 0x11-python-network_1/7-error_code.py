#!/usr/bin/python3
""" Sends a request to a URL and gets a response """
from sys import argv
import requests


if __name__ == '__main__':
    req = requests.get(argv[1])
    if req.status_code >= 400:
        print('Error code:', req.status_code)
    else:
        print(req.text)
