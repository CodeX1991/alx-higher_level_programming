#!/usr/bin/python3

j = 0

for n in range(0, 9):
    j = j + 1
    for m in range(j, 10):
        if n == 8 and m == 9:
            print("{}{}".format(n, m))
        else:
            print("{}{}".format(n, m), end=", ")
