#!/usr/bin/python3

"""function definition"""


def is_kind_of_class(obj, a_class):
    """
    Returns True or false depending on if obj is an instance of a_class

    Args:
       obj(object)
       a_class(the class)
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
