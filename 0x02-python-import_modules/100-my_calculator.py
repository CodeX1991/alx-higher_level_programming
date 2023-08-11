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
        if ch == argv[2]:
            if ch == '+':
                print("{} {} {} = {}".format(a, b, ch, add(a, b)))
            elif ch == '-':
                print("{} {} {} = {}".format(a, b, ch, sub(a, b)))
            elif ch == '*':
                print("{} {} {} = {}".format(a, b, ch, mul(a, b)))
            elif ch == '/':
                print("{} {} {} = {}".format(a, b, ch, div(a, b)))
            exit(0)
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
