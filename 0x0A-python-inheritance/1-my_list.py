#!/usr/bin/python3

"""a list that sorts"""


class MyList(list):
    """inherits from list but sorts"""

    def print_sorted(self):
        """returns sorted list"""

        print(sorted(self))
