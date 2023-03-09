#!/usr/bin/python3
"""Import calculator and run some calculation"""
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    suma = add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, suma))
    diff = sub(a, b)
    print("{:d} - {:d} = {:d}".format(a, b, diff))
    prod = mul(a, b)
    print("{:d} * {:d} = {:d}".format(a, b, prod))
    divi = div(a, b)
    print("{:d} / {:d} = {:d}".format(a, b, divi))
