#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns a key with the biggest integer value

    Args:
        a_dictionary: the dictionary to operatee on

    Return:
        the key if found or NOne otherwise
    """
    if a_dictionary is None:
        return None

    _value = sorted(a_dictionary.values())
    _max = max(_value)

    for k, v in a_dictionary.items():
        if v == _max:
            return k
