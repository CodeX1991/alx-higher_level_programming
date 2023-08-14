#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """Add 2 tuples

    Args:
        tuple_a: the first tuples
        tuple_b: the second tuples
    Return:
        sum of the 2 tuples
    """
    if tuple_a or tuple_b:
        if len(tuple_a) < 2 and len(tuple_a) != 0:
            return (tuple_a[0] + tuple_b[0], tuple_b[1])
        if len(tuple_b) < 2 and len(tuple_b) != 0:
            return (tuple_a[0] + tuple_b[0], tuple_a[1])
        if len(tuple_a) >= 2 and len(tuple_b) >= 2:
            return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        if len(tuple_a) == 0:
            return tuple_b
        if len(tuple_b) == 0:
            return tuple_a
