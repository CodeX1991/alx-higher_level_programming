#!/usr/bin/python3

"""An Input and Output Module"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object

    Args:
        my_obj: the given object to work with

    Return:
        the JSON representation of an object
    """

    return json.dumps(my_obj)
