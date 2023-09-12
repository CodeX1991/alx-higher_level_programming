#!/usr/bin/python3

"""A function module"""


def add_attribute(class_name, attr_name, attr_value):
    """Add attribute function

    Args:
        class_name: thw class to work with
        attr_name: the attribute name to add
        attr_value: what to add
    """

    try:
        setattr(class_name, attr_name, attr_value)
    except Exception:
        raise TypeError("can't add new attribute")
