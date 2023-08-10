#!/usr/bin/python3

import dis


def magic_calculation(a, b):
    """ Running a bytcode """

    return 98 + a ** b


dis.dis(magic_calculation)
