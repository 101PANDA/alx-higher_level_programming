#!/usr/bin/python3

"""defining a class rectangle"""


class Rectangle:
    """a class rectangle"""

    def __init__(self, width=0, height=0):
        """initializing a rectangle

        args:
          width and rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the width of the rectamgle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the heigth"""

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
