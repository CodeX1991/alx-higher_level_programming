#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Prints an integer with {:d}.format

    Args:
        value; can be any type

    Return: True if value has been corrected printed
    otherwise False
    """
    status = True
    try:
        print("{:d}".format(value))
    except Exception as err:
        print("Exception:", err, file=sys.stderr)
        status = False
    finally:
        return status
