#!/usr/bin/python3

def no_c(my_string):
    i = 0
    for x in my_string:
        if x == "C" or x == "c":
            my_string = my_string[:i] + my_string[(i+1):]
            i -= 1
        i += 1
    return my_string
