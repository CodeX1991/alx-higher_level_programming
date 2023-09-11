#!/usr/bin/python3

"""A module class"""


class BaseGeometry(object):
    """An empty class"""

    def area(self):
        """Raises exception message"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """Validate value"""
        if type(value) is str:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
