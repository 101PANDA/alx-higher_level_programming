#!/usr/bin/python3
"""Find multiples of of 2 in a list
   Assumes all input will always be a list containing int
   return True or False depending on whether the
   integer at the same position in the original list is a multiple of 2"""


def divisible_by_2(my_list=[]):
    if my_list == []:
        return []
    result_list = []
    for x in my_list:
        if x % 2 == 0:
            result_list.append(True)
        else:
            result_list.append(False)
    return result_list
