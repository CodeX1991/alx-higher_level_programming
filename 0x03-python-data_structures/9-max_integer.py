#!/usr/bin/python3

def max_integer(my_list=[]):
    """Finds the biggest integer of a list

    Args:
        my_list: the list to work with

    Return:
        None if my_list is empty
        otherwise return the biggest number
    """
    if len(my_list) == 0:
        return None
    _max = -99999
    for i in range(len(my_list)):
        if my_list[i] > _max:
            _max = my_list[i]
    return _max
