#!/usr/bin/python3

""" print and list outall arguments"""


if __name__ == "__main__":

    import sys

    av = sys.argv
    arglen = len(sys.argv) - 1

    if arglen == 0:
        print("{:d} arguments.".format(arglen))

    elif arglen == 1:
        print("{:d} argument:".format(arglen))

    else:
        print("{:d} arguments:".format(arglen))

    for i in range(arglen):
        if arglen == 0:
            break
        print("{}: {}".format(i + 1, av[i + 1]))
