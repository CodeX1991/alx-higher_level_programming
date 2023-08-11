#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    if len(argv) > 2:
        print("{} arguments:".format(len(argv) - 1))
        for n in range(1, len(argv)):
            print("{}: {}".format(n, argv[n]))
    if len(argv) == 1:
        print("{} arguments.".format(0))
    if len(argv) == 2:
        print("{} argument:".format(len(argv) - 1))
        print("{}: {}".format(len(argv) - 1, argv[1]))
