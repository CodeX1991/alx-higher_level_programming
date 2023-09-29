#!/usr/bin/python3

"""An Input and Output Module"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing a
    specific string

    Args:
        filename: the file to worrk with
        search_string: the string to search for
        new_string: the string to insert
    """

    with open(filename, 'r', encoding="utf-8") as old_file:
        text = old_file.readlines()
        new_text = []

    for line in text:
        new_text.append(line)

        if search_string in line:
            new_text.append(new_string)

    with open(filename, 'w', encoding="utf-8") as new_file:
        for line in new_text:
            new_file.write(line)
