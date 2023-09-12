#!/usr/bin/python3

"""An Input and Output Module"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout

    Args:
        filename: the name of the file
    """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
