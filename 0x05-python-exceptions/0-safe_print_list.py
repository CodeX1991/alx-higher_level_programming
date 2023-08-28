#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints x element of a list

    Args:
        my_list: the list to print from
        x: the number of element to print out

    Return: the actual number printed out
    """
    try:
        size_of_list = 0

        for elem in my_list:
            size_of_list += 1

        if x > size_of_list:
            x = size_of_list
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
        print('\n')
        return x
    except Exception:
        pass
