__author__ = 'mazzzy'

import unittest
import re

class MyTestCase(unittest.TestCase):

    def test_something(self):
        # my regex:
        p = re.compile('^(abc|acab|acabababc|ababab)$')

        positives = ['abc', 'acab', 'acabababc','ababab']
        negative = 'abcababc'
        for positive in positives:
            self.assertTrue(p.match(positive), "Did not match for {}".format(positive))
        self.assertFalse(p.match(negative))

if __name__ == '__main__':
    unittest.main()
