#!/usr/bin/python3

"""a list that sorts"""


class MyList(list):
    """inherits from list but sorts"""
    def __init__(self):
        """initialization"""
        list.__init__(self)

    def print_sorted(self):
        """returns sorted list"""

        print(sorted(self))
