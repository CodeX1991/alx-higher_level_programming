#!/usr/bin/python3
"""
A script that fetches a url
"""

from urllib.request import urlopen, Request

# Shouldnot execute when imported
if __name__ == "__main__":
    req = Request('https://alx-intranet.hbtn.io/status')

    with urlopen(req) as res:
        content = res.read()
        utf8_content = content.decode('utf8')

        # Print out the response
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(utf8_content))
