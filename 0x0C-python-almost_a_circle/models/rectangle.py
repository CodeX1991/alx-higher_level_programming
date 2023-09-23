#!/usr/bin/python3
"""A class module"""

from models.base import Base


class Rectangle(Base):
    """Declaring a Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id)

        self.validate_param(width, 'width')
        self.validate_param(height, 'height')
        self.validate_param(x, 'x')
        self.validate_param(y, 'y')

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
        self.validate_param(param, 'width')
        self.__width = param

    @property
    def height(self):
        """Retrieve the height"""
        return self.__height

    @height.setter
    def height(self, param):
        """set the height"""
        self.validate_param(param, 'height')
        self.__height = param

    @property
    def x(self):
        """Retrieve the x"""
        return self.__x

    @x.setter
    def x(self, param):
        """set the height"""
        self.validate_param(param, 'x')
        self.__x = param

    @property
    def y(self):
        """Retrieve the height"""
        return self.__y

    @y.setter
    def y(self, param):
        """set the height"""
        self.validate_param(param, 'y')
        self.__y = param

    def validate_param(self, value, param):
        """validate parameter"""
        if type(value) is not int:
            raise TypeError(param + " must be an integer")

        if value <= 0 and param in ('width', 'height'):
            raise ValueError(param + " must be > 0")

        if value < 0 and param in ('x', 'y'):
            raise ValueError(param + " must be >= 0")

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with character #"""
        if self.__y > 0:
            print('\n' * self.__y, end='')
        for i in range(self.__height):
            if self.__x > 0:
                print(' ' * self.__x, end='')
            for j in range(self.__width):
                if j == self.__width - 1:
                    print('#')
                else:
                    print('#', end="")

    def __str__(self):
        """Return a customize print out"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        argc = len(args)
        kwargsc = len(kwargs)

        if argc > 5:
            argc = 5
        if kwargsc > 5:
            kwargsc = 5

        modif_attr = ['id', 'width', 'height', 'x', 'y']

        if argc > 0:
            for i in range(argc):
                setattr(self, modif_attr[i], args[i])
        elif kwargsc > 0:
            for key, value in kwargs.items():
                if key in modif_attr:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
