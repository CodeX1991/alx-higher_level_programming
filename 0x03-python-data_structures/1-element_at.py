#!/usr/bin/python3

def element_at(my_list, idx):
    """Retrieves an element from a list like in C

    Args:
        my_list: the given list to work with it
        idx: the given index to retrieve

    Return:
        None if idx is negative
        None if idx is out of range
    """
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    else:
        return my_list[idx]
