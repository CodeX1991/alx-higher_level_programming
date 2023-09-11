#!/usr/bin/python3

"""A class module"""


def is_same_class(obj, a_class):
    """Verify if it is an object

    Args:
        obj: the object to work with
        a_class: the class to work with

    Return:
        True or False
    """
    if type(obj) == a_class:
        return True
    else:
        return False
