#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Prints x element of a list

    Args:
        my_list: the list to print from
        x: the number of element to print out

    Return: the actual number printed out
    """
    lenList = 0
    idx = 0
    for i in my_list:
        lenList += 1
    if x != 0 and lenList:
        for i in range(x):
            if type(my_list[i]) is int:
                try:
                    print("{:d}".format(my_list[i]), end="")
                    idx += 1
                except IndexError as err:
                    print(err)
        print()
    return idx
