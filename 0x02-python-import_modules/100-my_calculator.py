#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    my_arg = len(sys.argv) - 1
    if my_arg != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    my_oper = sys.argv[2]
    if my_oper != '-' and my_oper != '+' and my_oper != '/' and my_oper != '*':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    from calculator_1 import mul, add, sub, div
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if my_oper == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif my_oper == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif my_oper == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))