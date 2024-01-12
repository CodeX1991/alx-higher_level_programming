#!/usr/bin/python3
"""
A script that takes in a url an email,
sends a POST request to the passed url with
the email as a parameter, and displays the body
of the response
"""

from sys import argv
import requests

# Shouldnot execute when imported
if __name__ == "__main__":
    # Create data variable
    payload = {'email': argv[2]}

    # Request for the url
    r = requests.post(argv[1], params=payload)
    print(r.text)
