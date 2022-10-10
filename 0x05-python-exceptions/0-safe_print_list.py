#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    num_printed = 0
    for x in range(x):
        try:
            list_type = type(my_list[x])
            print(list_type(my_list[x]), end='')
            num_printed += 1

        except IndexError:
            break
    print()
    return num_printed
