#!/usr/bin/python3

""" replace "search" with "replace" in "my_list" """


def search_replace(my_list, search, replace):
    new_list = []
    list_len = len(my_list)

    for x in range(0, list_len):
        if my_list[x] == search:
            new_list.append(replace)

        else:
            new_list.append(my_list[x])

    return new_list
