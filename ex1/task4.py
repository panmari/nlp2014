#!/usr/bin/python3


def fib(n):
    if n == 0:
        return 1
    else:
        return fib(n-1)*n

import sys

input = eval(sys.argv[1])

print("{} faculty is {}".format(input, fib(input)))