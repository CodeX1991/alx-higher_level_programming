#!/usr/bin/python3
"""
A script that takes in a url, send a request to the URL and
displays the value of the variable X-Request-Id in the response header
"""

from sys import argv
import requests

# Shouldnot execute when imported
if __name__ == "__main__":
    r = requests.get(argv[1])

    print(r.headers.get("X-Request-Id"))
