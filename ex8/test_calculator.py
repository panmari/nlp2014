
__author__ = 'mazzzy'

import unittest
from exercise_05 import parse_calculator_string
from pyparsing import ParseException

class MyTestCase(unittest.TestCase):
    def test_simple_addtion(self):
        self.assertEqual("['1', '+', '2']", str(parse_calculator_string('1 + 2')))

    def test_simple_multiplication(self):
        self.assertEqual("['1', '*', '2']", str(parse_calculator_string('1 * 2')))

    def test_multiple_terms(self):
        parsed = parse_calculator_string('1 * 2 + 3')
        self.assertEqual("['1', '*', '2', '+', '3']", str(parsed))

    def test_variable_names(self):
        parsed = parse_calculator_string('a * b')
        self.assertEqual("['a', '*', 'b']", str(parsed))

    def test_multiplication_with_negative_number(self):
        parsed = parse_calculator_string('1 * -2 + 3')
        self.assertEqual("['1', '*', '-2', '+', '3']", str(parsed))

    def test_starting_with_negative_number(self):
        parsed = parse_calculator_string('-2 + 3')
        self.assertEqual("['-2', '+', '3']", str(parsed))

    def test_invalid_calc_string_times(self):
        with self.assertRaises(ParseException):
            parse_calculator_string(' * -2 + 3')

    def test_invalid_calc_string_plus(self):
        with self.assertRaises(ParseException):
            parse_calculator_string(' + -2 + 3')


if __name__ == '__main__':
    unittest.main()
