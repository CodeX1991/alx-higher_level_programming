#!/usr/bin/python3
"""
A script that takes in a url,
sends a request to the url and
displays the value of the X-Request-Id
variable found in the header of the response
"""

from sys import argv
from urllib.request import urlopen, Request

# Shouldnot execute when imported
if __name__ == "__main__":
    req = Request(argv[1])

    with urlopen(req) as res:
        headers = res.info()
        print(headers.get("X-Request-Id"))
