#!/usr/bin/python3

"""An Input and Output Module"""
import json


def from_json_string(my_str):
    """Returns the JSON representation of an object

    Args:
        my_str: the given JSON object to work with

    Return:
        the str representation of a JSON object
    """

    return json.loads(my_str)
