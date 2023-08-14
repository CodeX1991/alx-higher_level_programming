#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Replaces an element of a list at a specific position

    Args:
        my_list: the list to work with
        idx: the index to work with
        element: the element to use for replacement

    Return:
        original list if idx < 0 or idx is out of range
        otherwise a new list
    """
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
        return my_list
    return my_list
