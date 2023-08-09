#!/usr/bin/python3

def fizzbuzz():
    """ Prints the numbers from 1 to 100 separated by a space """
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 != 0:
            print("{}".format("Fizz"), end=" ")
        elif n % 5 == 0 and n % 3 != 0:
            print("{}".format("Buzz"), end=" ")
        elif n % 15 == 0:
            print("{}".format("FizzBuzz"), end=" ")
        else:
            print("{}".format(n), end=" ")
