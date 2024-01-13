#!/usr/bin/python3
"""
List 10 commits (from recent to oldest)
of a repositiry by user

This script use the Github API and print all commits
by: `<sha>: <author name>` (one by line).
"""

from sys import argv
import requests

# Shouldnot execute when imported
if __name__ == "__main__":
    # Fetch the content
    url = 'https://api.github.com'
    uri = "{0}/repos/{1}/{2}/commits".format(url, argv[2], argv[1])
    r = requests.get(uri).json()

    for com in r[0:10]:
        print(com['sha'] + ':', com['commit']['author']['name'])
