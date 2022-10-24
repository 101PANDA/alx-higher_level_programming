#!/usr/bin/python3

"""a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ a class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """initializer
        Args:
            width
            height

        validates width & height with parent class funtion integer_validator
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns area of the rectangle
        """

        value = self.__width * self.__height
        return value

    def __str__(self):
        """str rep of func"""

        mess = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return mess
