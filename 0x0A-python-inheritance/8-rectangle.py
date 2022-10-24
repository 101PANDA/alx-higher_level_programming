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
        super.integer_validator("width", width)
        super.integer_validator("height", height)
        self.__width = width
        self.__height = height
