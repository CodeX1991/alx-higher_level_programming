#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys

    Args:
        a-dictionary: the dic to work with
    """
    converted_dict = dict(sorted(a_dictionary.items()))

    for k, v in converted_dict.items():
        print("{}: {}".format(k, v))
