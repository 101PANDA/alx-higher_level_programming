#!/usr/bin/python3

"""add all int from a list only ones"""


def uniq_add(my_list=[]):
    uniq_list = []
    added = 0

    for x in my_list:
        if x not in uniq_list:
            uniq_list.append(x)

    for i in uniq_list:
        added += i

    return added
