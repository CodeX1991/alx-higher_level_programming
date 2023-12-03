#!/bin/bash
# A script that takes in a URL and display all HTTP methods
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d':' -f2 | sed 's/ //'
