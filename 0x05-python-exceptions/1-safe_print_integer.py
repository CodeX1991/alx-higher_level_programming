#!/usr/bin/python3

def safe_print_integer(value):
    """Prints an integer with {:d}.format

    Args:
        value; can be any type

    Return: True if value has been corrected printed
    otherwise False
    """
    status = True
    try:
        print("{:d}".format(value))
    except Exception:
        status = False
    finally:
        return status
