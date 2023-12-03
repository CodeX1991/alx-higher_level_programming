#!/bin/bash
# A script that uses curl to send POST request to a URL
curl -sL -X POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
