#!/usr/bin/python3
"""
A script that takes in a url an email,
sends a POST request to the passed url with
the email as a parameter, and displays the body
of the response (decoded in utf-8)
"""

from sys import argv
from urllib.request import urlopen, Request
from urllib.parse import urlencode

# Shouldnot execute when imported
if __name__ == "__main__":
    # Create data variable
    data = {'email': argv[2]}
    data = urlencode(data).encode('ascii')

    # Request for the url
    req = Request(argv[1], data)

    with urlopen(req) as res:
        res = res.read().decode('utf-8')
        print(res)
