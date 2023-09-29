#!/usr/bin/python3

"""An Input and Output Module"""


def class_to_json(obj):
    """Returns the dictionary description

    Args:
        obj: the given JSON serialization object to work with

    Return:
        the dictionary representation of a JSON serialization of an object
    """

    return obj.__dict__
