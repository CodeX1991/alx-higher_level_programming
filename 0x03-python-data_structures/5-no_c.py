#!/usr/bin/python3

def no_c(my_string):
    """removes all characters c and C from a string

    Args:
        my_string: the string to work with

    Return:
        The new string
    """
    new_string = ""
    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            continue
        new_string += my_string[i]
    return new_string
