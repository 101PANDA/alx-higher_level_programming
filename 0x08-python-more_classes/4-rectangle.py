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


    def area(self):
        """returns the area of a rectangle
        formula:
           heigth * width
        """
        result = self.__height * self.__width
        return (result)

    def perimeter(self):
        """ returns the perimeter of a rectangle
        formula:
           2(height + width)
        if height or width is equal to 0, perimeter is equal to 0
        """
        if (self.__height == 0) or (self.__width == 0):
            result = 0
        else:
            result = 2 * (self.__height + self.__width)
        return (result)


    def __str__(self):
        """returns the printable representation of rectangle
        uses # to represent it
        """

        if (self.__height == 0) or (self.__width == 0):
            return ""
        else:
            rect = ""
            for x in range(self.__height):
                for i in range(self.__width):
                    rect = rect + "#"
                if x != (self.__height - 1):
                    rect = rect + "\n"
            return rect

    def __repr__(self):
        """return the string representation of the Rectangle"""
        func = "Rectangle(" + str(self.__width)
        func += ", " + str(self.__height) + ")"
        return func
