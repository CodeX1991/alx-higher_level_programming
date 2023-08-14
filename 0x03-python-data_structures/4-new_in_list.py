#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """replaces an element in a list at a specific position
    without modifying the original list

    Args:
        my_list: the given list to work with
        idx: the index to work with
        element: the replacing data

    Return:
        original list if idx < 0 or idx > len(my_list)
        otherwise a copy of the replaced list
    """
    new_list = []

    if idx >= 0 and idx < len(my_list):
        for i in range(len(my_list)):
            new_list.append(my_list[i])
        new_list[idx] = element
        return new_list
    return my_list
