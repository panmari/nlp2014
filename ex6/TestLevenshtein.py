__author__ = 'mazzzy'

import unittest
from ex6.exercise_04 import damerauLevenshtein

class SomeLevenshteinTests(unittest.TestCase):

    def test_something(self):
        s = damerauLevenshtein()
        self.assertEqual(0, s.compute('then', 'then'))
        self.assertEqual(1, s.compute('then', 'tehn'))
        self.assertEqual(1, s.compute('then', 'thn'))
        self.assertEqual(1, s.compute('then', 'theen'))


if __name__ == '__main__':
    unittest.main()
