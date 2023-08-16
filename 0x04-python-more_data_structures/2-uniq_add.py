#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Adds all unique integers in a list (only once for each integer)

    Args:
        my_list: list to work with
    Return:
        the sum of unique data on success
    """
    return sum(set(my_list))
