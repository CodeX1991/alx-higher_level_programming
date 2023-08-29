#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints x element of a list

    Args:
        my_list: the list to print from
        x: the number of element to print out

    Return: the actual number printed out
    """
    idx = 0

    try:
        for i in my_list:
            if idx < x:
                if idx == x - 1:
                    print("{}".format(my_list[idx]))
                else:
                    print("{}".format(my_list[idx]), end="")
                idx += 1
    except Exception:
        pass
    finally:
        return idx
