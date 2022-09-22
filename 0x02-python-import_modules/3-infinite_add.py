#!/usr/bin/python3

"""sum of any setof numbers"""
if __name__ == "__main__":
    import sys

    total = 0

    count = len(sys.argv) - 1

    for i in range(count):
        total += int(sys.argv[i + 1])


    print("{:d}".format(total))
