#!/usr/bin/python3


print("Please enter an integer")
try:
    input_int = eval(input())
except NameError as e:
    print("Oops, that was not an integer!")
    exit(1)

print("The first {} numbers of the fibonacci sequence are: ".format(input_int))
fib = [1,1]
for i in range(input_int):
    fib.append(fib[-1] + fib[-2])

print(fib)
