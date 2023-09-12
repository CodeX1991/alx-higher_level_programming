#!/usr/bin/python3

"""An Input and Output Module"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file, using a JSON representation

    Args:
        my_obj: the given JSON object to work with
        filename: the file to write to
    """

    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
