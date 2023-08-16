#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """Return a set of all elements present in only one set

    Args:
        set_1: the firest set
        set_2: the second set
    Return:
        List of common element
    """
    return set_1 ^ set_2
