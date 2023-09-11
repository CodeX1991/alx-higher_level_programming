#!/usr/bin/python3
"""A class module"""


class MyList(list):
    """This class inherit from list"""

    def print_sorted(self):
        """Prints the list sorted in ascending order"""

        if issubclass(MyList, list) is True:
            print(sorted(self))
        if issubclass(MyList, list) is False:
            raise AttributeError
