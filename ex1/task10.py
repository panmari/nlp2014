#!/usr/bin/python3


from ex1.my_complex import MyComplex

import sys

def print_help(do_exit=True):
    print("Usage: ./task10.py [real part x1] [imaginary part x1] [real part x2] [imaginary part x2]")
    if do_exit:
        sys.exit(1)

args = sys.argv
if len(args) != 5:
    print("Not correct number of arguments")
    print_help()

try:
    #convert input to numbers except first argument (name of script)
    args_eval = [eval(x) for x in args[1:]]
except:
    print('Could not convert to numbers!')
    print_help()

x1 = MyComplex(args_eval[0], args_eval[1])
x2 = MyComplex(args_eval[2], args_eval[3])

with open("results.txt", 'w') as f:
    f.write("x1: {}\n".format(str(x1)))
    f.write("x2: {}\n".format(str(x2)))
    f.write("Addition: {}\n".format(str(x1+x2)))
    f.write("Subtraction: {}\n".format(str(x1-x2)))

print("Successfully wrote results.txt")