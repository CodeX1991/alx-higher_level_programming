#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints x element of a list

    Args:
        my_list: the list to print from
        x: the number of element to print out

    Return: the actual number printed out
    """
    lenList = 0
    for i in my_list:
        lenList += 1

    if x > lenList:
        x = lenList

    if x != 0 and lenList:
        try:
            for n in range(0, x):
                if n == x - 1:
                    print("{}".format(my_list[n]))
                else:
                    print("{}".format(my_list[n]), end="")
        except Exception:
            pass
    return x
