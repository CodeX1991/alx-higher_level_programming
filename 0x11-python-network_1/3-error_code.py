#!/usr/bin/python3
"""
A script that takes in a url, sends a request
to the url and displays the body of the response
(decoded in utf-8)
"""

from sys import argv
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from urllib.error import HTTPError

# Shouldnot execute when imported
if __name__ == "__main__":
    # Request for the url
    req = Request(argv[1])

    try:
        with urlopen(req) as res:
            res = res.read().decode('utf-8')
            print(res)
    except HTTPError as e:
        print("Error code:", e.code)
