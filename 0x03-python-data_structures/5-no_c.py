#!/usr/bin/python3

def no_c(my_string):
    i, b = 0, 1
    for x in my_string:
        if x == "c" or x == "C":
            my_string = my_string[:i] + my_string[(i+1):]

        return my_string
