#!/usr/bin/python3
"""
A script that fetches a url
"""

import requests

# Shouldnot execute when imported
if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')

    # Print out the response
    print("Body response:")
    print("\t- type: {}".format(type(r.headers['content-type'])))
    print("\t- content: {}".format(r.text))
