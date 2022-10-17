#!/usr/bin/python3

def add_integer(a, b=98):

    """
    returns the addition of two integers either exact integer or float

    a type error is raised if a or b isn't an integer

    all floats are casted to int before addition
    """

    if ((not isinstance(a, int) and (not isinstance(a, float)))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and (not isinstance(b, float)))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
