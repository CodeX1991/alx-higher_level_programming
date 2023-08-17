#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """deletes a key in a dictionary

    Args:
        a_dictionary: the dictionary to work with
        key: the key to delete

    Return:
        updated dictionary
    """
    for k in a_dictionary:
        if k == key:
            del a_dictionary[key]
            return a_dictionary
    return a_dictionary
