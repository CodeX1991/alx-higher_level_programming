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

    @property
    def width(self):
        """Retrieve the width"""
        return self.__width

    @width.setter
    def width(self, param):
        """Set the width"""
        self.__width = param

    @property
    def height(self):
        """Retrieve the height"""
        return self.__height

    @height.setter
    def height(self, param):
        """set the height"""
        self.__height = param

    @property
    def x(self):
        """Retrieve the x"""
        return self.__x

    @x.setter
    def x(self, param):
        """set the height"""
        self.__x = param

    @property
    def y(self):
        """Retrieve the height"""
        return self.__y

    @y.setter
    def y(self, param):
        """set the height"""
        self.__y = param
