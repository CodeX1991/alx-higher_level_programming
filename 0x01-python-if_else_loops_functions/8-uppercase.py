#!/usr/bin/python3

def uppercase(str):
    """Prints str in uppercases"""
    newStr = ""
    for ch in range(len(str)):
        if ord(str[ch]) >= 97 and ord(str[ch]) <= 122:
            newStr += chr(ord(str[ch]) - 32)
            continue
        newStr += str[ch]
    print("{}".format(newStr))
