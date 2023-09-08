#!/usr/bin/python3
"""A Module that print #"""


def print_square(size):
    """Prints a square with the character

    Args:
        size: the size to work with
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    my_print(size)


def my_print(size):
    """Prints to the stdout the square with the character #"""
    if size == 0:
        print()
        return None

    for i in range(0, size * size):
        if i % size == 0 and i > 0:
            print()
        if i == size * size - 1:
            print('#')
        else:
            print('#', end='')
