#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """Replaces or adds key/value in a dictionary

    Args:
        a_dictionary: dictionary to work with
        key: the key to work with
        value: the value to replace or add

    Return:
        the updated dictionary
    """
    for k in a_dictionary:
        if k == key:
            a_dictionary[k] = value
            return a_dictionary
    a_dictionary[key] = value
    return a_dictionary
