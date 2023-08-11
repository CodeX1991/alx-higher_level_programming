#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    from calculator_1 import add, sub, mul, div

    str_ch = "+-*/"
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    for ch in str_ch:
        if ch != argv[2]:
            continue
        if ch == argv[2]:
            break
    if ch != argv[2]:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if ch == '+':
        print("{} {} {} = {}".format(a, ch, b, add(a, b)))
    elif ch == '-':
        print("{} {} {} = {}".format(a, ch, b, sub(a, b)))
    elif ch == '*':
        print("{} {} {} = {}".format(a, ch, b, mul(a, b)))
    elif ch == '/':
        print("{} {} {} = {}".format(a, ch, b, div(a, b)))
