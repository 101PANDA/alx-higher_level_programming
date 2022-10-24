#!/usr/bin/python3
""" a class BaseGeometry"""


class BaseGeometry:
    """Represent base geometry
    Raises exception on call to area"""

    def area(self):
        """raising exception"""
        raise Exception("area() is not implemented")
