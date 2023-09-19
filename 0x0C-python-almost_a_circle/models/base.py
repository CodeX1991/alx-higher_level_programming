#!/usr/bin/python3

"""
A nodule that contains a Base class to
manage the id attribute of all classes that
extend from Base and avoid duplicate the same code

"""


class Base:
    """A base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
