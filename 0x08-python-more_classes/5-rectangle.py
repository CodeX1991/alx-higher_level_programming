#!/usr/bin/python3

"""Declare a module with the Rectangle class"""


class Rectangle:
    """A class Rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize the class attribute"""
        self.__width = width
        self.__height = height

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        """Retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __draw_rectangle(self):
        """Draw the rectangle using #

        Return:
            an empty string is width or height is 0
            otherwise the string with the rectangle
        """
        w = self.__width
        h = self.__height
        re_str = ''

        if w == 0 or h == 0:
            return re_str

        for i in range(h):
            for j in range(w):
                re_str += '#'
            if i != h - 1:
                re_str += '\n'
        return re_str

    def __str__(self):
        """Return a string with the representation of the Rectangle"""
        return self.__draw_rectangle()

    def __repr__(self):
        """Return a representation of the Rectangle"""
        w = str(eval('self.width'))
        h = str(eval('self.height'))

        return 'Rectangle(' + w + ', ' + h + ')'

    def __del__(self):
        """Display when del keyword is called"""
        print("Bye rectangle...")
