#!/usr/bin/python3
"""
A script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""

from sys import argv
import requests

# Shouldnot execute when imported
if __name__ == "__main__":
    # Check of number of arg
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""

    # Make a post request
    try:
        payload = {"q": q}
        r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
        r = r.json()

        if {'id', 'name'} <= r.keys():
            print("[{}] {}".format(r.get('id'), r.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
