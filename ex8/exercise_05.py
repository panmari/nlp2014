from pyparsing import *
import sys


def parse_calculator_string(s):
    plusorminus = Literal('+') | Literal('-')
    number = Word("0123456789")
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
    return expr.parseString(s)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        s = ' 4 * 53 - 1 + b + 3 * a * -1'
        print('You need to provide a command line argument, doing default string: {}'.format(s))
    else:
        s = sys.argv[1]

    print(parse_calculator_string(s))