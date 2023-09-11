#!/usr/bin/python3

def lookup(obj):
    """Returns the list of available attributes and methods of an object

    Args:
        obj: the object to work with
    """
    return dir(obj)
