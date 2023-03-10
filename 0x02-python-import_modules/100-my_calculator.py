#!/usr/bin/python3
"""Import calculator"""
"""Then becomes a calculator"""

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if sys.argv[2] not in {"+", "-", "*", "/"}:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]
    if operator == "+":
        total = add(a, b)
    elif operator == "-":
        total = sub(a, b)
    elif operator == "*":
        total = mul(a, b)
    elif operator == "/":
        total = div(a, b)
    print("{:d} {} {:d} = {:d}".format(a, operator, b, total))
