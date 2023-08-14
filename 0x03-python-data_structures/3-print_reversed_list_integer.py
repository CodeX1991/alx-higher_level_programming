#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list, in reverse order

    Args:
        my_list: the given list to work with
    """
    if my_list:
        for i in range(1, (1 + len(my_list))):
            i = -i
            print("{:d}".format(my_list[i]))
