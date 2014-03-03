#!/usr/bin/python3


def f(x):
    return g(x) + 1


def g(x):
    return 1 / x


### main
try:
    print(f(0))
except ZeroDivisionError as e:
    print("Division by zero is not allowed!")
