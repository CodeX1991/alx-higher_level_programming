#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    idx = len(my_list) - 1
    for n in my_list:
        if idx >= 0:
            print("{:d}".format(my_list[idx]))
        idx = idx - 1
