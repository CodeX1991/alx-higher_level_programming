#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by another in a new list

    Args:
        my_list: is the initial list
        search: is the element to replace in the list
        replace: is the new element
    Return:
        the new list
    """
    if my_list:
        new_list = []
        for n in my_list:
            if n == search:
                n = replace
            new_list.append(n)
        return new_list
