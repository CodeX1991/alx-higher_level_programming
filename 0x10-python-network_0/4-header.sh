#!/bin/bash
# A script that uses curl to send a request to an url with X-School-User-Id=98
curl -sL -X GET "$1" -H "X-School-User-Id: 98"
