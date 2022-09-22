#!/usr/bin/python3
if __name__ == "__main__":
    import add_0 as adder
    a = 1
    b = 2
    sum = adder.add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, sum))
