#!/usr/bin/python3

"""A class module"""


def is_kind_of_class(obj, a_class):
    """Verify if it is an object

    Args:
        obj: the object to work with
        a_class: the class to work with

    Return:
        True or False
    """
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
