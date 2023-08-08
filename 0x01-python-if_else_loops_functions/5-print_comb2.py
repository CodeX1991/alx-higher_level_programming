#!/usr/bin/python3

sep = ", "
for n in range(0, 100):
    if n == 99:
        sep = "\n"
    if n >= 0 and n < 10:
        print("{}{}".format(0, n), end=sep)
    else:
        print("{}".format(n), end=sep)
