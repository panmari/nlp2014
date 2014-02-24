#!/usr/bin/python3

print("Please give a string as input")
# PEP 3111: raw_input() was renamed to input(). That is, the new input() function reads a line
# from sys.stdin and returns it with the trailing newline stripped. It raises EOFError if the
# input is terminated prematurely. To get the old behavior of input(), use eval(input()).
input_string = input()
print("Your string in reverse with one letter per line:")
for l in input_string[::-1]:
    print(l)
