__author__ = 'mazzzy'

import unittest
from ex6.exercise_04 import soundex

class MyTestCase(unittest.TestCase):

    def test_something(self):
        s = soundex()
        self.assertEqual('T620', s.encode('Trough'))
        self.assertEqual('T200', s.encode('Though'))
        self.assertEqual('P450', s.encode('Plane'))
        self.assertEqual('P450', s.encode('Plain'))
        self.assertEqual('M600', s.encode('Mayor'))
        self.assertEqual('M600', s.encode('Marrow'))

if __name__ == '__main__':
    unittest.main()
