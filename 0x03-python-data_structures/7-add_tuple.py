#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a == ():
        tuple_a = 0, 0

    if tuple_b == ():
        tuple_b = 0, 0

    a = tuple_a[0] + tuple_b[0]
    if len(tuple_a) < 2 and len(tuple_b) >= 2:
        b = 0 + tuple_b[1]

    if len(tuple_b) < 2 and len(tuple_a) >= 2:
        b = 0 + tuple_a[1]

    if len(tuple_b) < 2 and len(tuple_a) < 2:
        b = 0

    if len(tuple_b) >= 2 and len(tuple_a) >= 2:
        b = tuple_a[1] + tuple_b[1]

    new_tuple = a, b
    return new_tuple
