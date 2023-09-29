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

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation"""
        class_d = self.__dict__
        sel_d = dict()

        if type(attrs) is list:
            for attr in attrs:
                if type(attr) is not str:
                    return class_d

                if attr in class_d:
                    sel_d[attr] = class_d[attr]
            return sel_d
        return class_d
