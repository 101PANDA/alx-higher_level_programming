#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        return None
    _list = my_list.copy()
    _list.sort()
    max_val = _list.pop()
    return max_val
