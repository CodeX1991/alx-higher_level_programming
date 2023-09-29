#!/usr/bin/python3

"""An Input and Output Module"""


class Student:
    """Student class

    Attributes:
        first_name: student first name
        last_name: student last name
        age: student age
    """

    def __init__(self, first_name, last_name, age):
        """Instantiate the variable"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation"""
        return self.__dict__
