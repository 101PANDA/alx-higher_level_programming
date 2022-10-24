#!/usr/bin/python3

"""function definition"""


def is_same_class(obj, a_class):
    """Returns True if obj is same class as a_class
    args:
        obj(any object) - object being checked
        a_class(any class) - class being assesed
    """

    if type(obj) == a_class:
        return True
    else:
        return False
