#!/usr/bin/python3
"""
A python script that takes your GitHub credentials
(username and password) and uses the GitHub
API to display your id
"""

from sys import argv
import requests

# Shouldnot execute when imported
if __name__ == "__main__":
    # Fetch the content
    url = 'https://api.github.com/users'
    r = requests.get(url, auth=(argv[1], argv[2]))
    r = r.json()

    print(r.get('id'))
