#!/usr/bin/python3

class BaseGeometry:
    """Represent base geometry
    Raises exception on call to area"""

    def area(self):
        """raising exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
