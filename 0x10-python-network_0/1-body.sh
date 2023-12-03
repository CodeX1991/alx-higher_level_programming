#!/bin/bash
# A script that uses curl to send a request to an url
curl -sL -X GET "$1" -D ./header -o ./output; if grep -q "200 OK" ./header; then cat ./output; fi
