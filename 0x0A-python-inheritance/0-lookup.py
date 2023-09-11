#!/usr/bin/python3
"""A module that return a list"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object

    Args:
        obj: the object to work with
    """
    return dir(obj)
