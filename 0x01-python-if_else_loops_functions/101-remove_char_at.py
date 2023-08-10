#!/usr/bin/python3

def remove_char_at(str, n):
    """ Creates a copy of the string str,
    removing the character at the position n
    """
    copied_str = ""

    for i in range(len(str)):
        if i == n:
            continue
        copied_str += str[i]
    copied_str += '\0'
    return copied_str
