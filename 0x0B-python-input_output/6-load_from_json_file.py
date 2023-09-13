#!/usr/bin/python3

"""An Input and Output Module"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file

    Args:
        filename: the file to work with
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.loads(f.read())
