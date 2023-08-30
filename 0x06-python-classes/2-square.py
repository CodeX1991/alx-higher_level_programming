#!/usr/bin/python3

"""Defining a module with the class Sqaure"""


class Square:
    """Define a square"""
    def __init__(self, size=0):
        """Initializes the data

        Attributes:
            size(:obj:`int', optional): the size to work with

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
