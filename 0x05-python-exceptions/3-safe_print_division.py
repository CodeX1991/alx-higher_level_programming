#!/usr/bin/python3

def safe_print_division(a, b):
    """Divides 2 integers and prints the result

    Args:
        a: dividened
        b: divisor

    Return: the value of the division, otherwise: None
    """
    result = 0
    try:
        result = a / b
    except Exception:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
