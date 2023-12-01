#!/usr/bin/python3
""" sends a request to a website """
import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        data = response.read()
        print(f"Body response:")
        print(f"\t- type: {type(data)}")
        print(f"\t- uft8 content: {data.decode('utf-8')}")
