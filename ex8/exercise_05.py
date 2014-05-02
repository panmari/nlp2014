from pyparsing import *
import sys

# define grammar
plusorminus = Literal('+') | Literal('-')
number = Word(nums)
# plus/minus is attached to number/variable, so we don't run into problems with multiplication and/or addition
integer = Combine(Optional(plusorminus) + number)
variable = Combine(Optional(plusorminus) + Word(alphas))

plus = Literal("+")
minus = Literal("-")
mult = Literal("*")
div = Literal("/")
addop = plus | minus
multop = mult | div
atom = integer | variable

factor = Forward()
factor << atom + ZeroOrMore(factor)

term = factor + ZeroOrMore(multop + factor)
expr = term + ZeroOrMore(addop + term)

if len(sys.argv) == 1:
    s = '1+4*53-1+b+3*a'
    print('You need to provide a command line argument, doing default string: {}'.format(s))
else:
    s = sys.argv[1]

print(expr.parseString(s))