#!/usr/bin/python3

"""An Input and Output Module"""


def append_write(filename="", text=""):
    """Reads a text file and prints it to stdout

    Args:
        filename: the name of the file
        text: test to write the filename

    Return:
        the number of characters written
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
