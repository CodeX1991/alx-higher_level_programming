#!/usr/bin/python3

count = 25
for n in range(97, 123):
    if n % 2 == 0:
        n = n - 32
    print("{}".format(chr(n + count)), end="")
    count -= 2
