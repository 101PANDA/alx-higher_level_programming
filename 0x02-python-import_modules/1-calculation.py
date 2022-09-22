#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as cal
    a = 10
    b = 5
    suma = cal.add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, suma))
    diff = cal.sub(a, b)
    print("{:d} - {:d} = {:d}".format(a, b, diff))
    prod = cal.mul(a, b)
    print("{:d} * {:d} = {:d}".format(a, b, prod))
    divi = cal.div(a, b)
    print("{:d} / {:d} = {:d}".format(a, b, divi))
