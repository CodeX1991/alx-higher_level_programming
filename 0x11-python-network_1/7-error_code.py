#!/usr/bin/python3
"""
A script that takes in a url, sends a request to the url
and displays the body of the response
"""

from sys import argv
import requests

# Shouldnot execute when imported
if __name__ == "__main__":
    # Request for the url
    r = requests.get(argv[1])

    if r.status_code >= 400:
        print("Error code:", r.status_code)
    else:
        print(r.text)
