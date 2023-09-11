#!/usr/bin/python3

"""A class module"""


def inherits_from(obj, a_class):
    """Verify if it is an object

    Args:
        obj: the object to work with
        a_class: the class to work with

    Return:
        True or False
    """
    if isinstance(obj, a_class) and \
            issubclass(a_class, obj.__class__) is False:
        return True
    else:
        return False
