#!/usr/bin/python3
"""A class module"""

from models.base import Base


class Rectangle(Base):
    """Declaring a Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
