#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multiplied by 2

    Args:
        a_dictionary: the dictionary to work with

    Return:
        a new updated dictionary
    """
    new_dict = a_dictionary.copy()

    for k, value in new_dict.items():
        new_dict[k] = value * 2
    return new_dict
