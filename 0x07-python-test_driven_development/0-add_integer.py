#!/usr/bin/python3
"""Module documnetation"""


def add_integer(a, b=98):
    """Adds 2 integers

    Args:
        a: first integer
        b: second integer

    Raises:
        TypeError: if a or b is not int

    Return:
        the addition of a and b
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")

    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return (a + b)
