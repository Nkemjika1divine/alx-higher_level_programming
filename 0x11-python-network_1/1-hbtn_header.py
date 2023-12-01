#!/usr/bin/python3
""" mSends a request and gets a response """
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.info()["X-Request-Id"])
