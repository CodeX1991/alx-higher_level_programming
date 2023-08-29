#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Prints an integer with {:d}.format

    Args:
        fct: pointer to a function
        args: pointer to list of argument passed to the function

    Return: the result of the otherwise None if something happens during
    the function and prints in stderr the error precede by Exception:
    """
    result = None
    try:
        result = fct(*args)
    except Exception as err:
        print("Exception:", err, file=sys.stderr)
    return result
