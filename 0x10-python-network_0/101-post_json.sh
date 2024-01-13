#!/bin/bash
# Send a JSON POST rquest to a url
curl -s "$1" -X POST -H "Content-Type: application/json" -d "$(cat "$2")"
