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

    def area(self):
        """Define the area of the sqaure

        Return: areas of the square
        """
        return (self.__size * self.__size)

    def my_print(self):
        """Prints to the stdout the square with the character #"""
        if self.__size == 0:
            print()
            return None

        for i in range(0, self.area()):
            if i % self.__size == 0 and i > 0:
                print()
            if i == self.area() - 1:
                print('#')
            else:
                print('#', end='')

    @property
    def size(self):
        """retrieve the set value

        Attributws:
            value: the value to set t
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size to value

        Attributes:
            value: the value to set to
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
