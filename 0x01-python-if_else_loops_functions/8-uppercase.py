#!/usr/bin/python3

def uppercase(str):
    """Prints str in uppercases"""
    sep = ""
    strLen = len(str)
    count = 0
    for ch in str:
        if count == strLen - 1 or strLen == 0:
            sep = '\n'
        if ord(ch) >= 97 and ord(ch) <= 122:
            print("{}".format(chr(ord(ch) - 32)), end=sep)
        else:
            print("{}".format(ch), end=sep)
        count = count + 1
