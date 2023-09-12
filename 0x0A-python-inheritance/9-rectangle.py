#!/usr/bin/python3
"""A class module"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Declaring a class"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return a customize print out"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
