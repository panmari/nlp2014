

import unittest
import re


class MyTestCase(unittest.TestCase):



    def test_something(self):
        p = re.compile('(?=[^A-Z])[^0-9,\.]{5,}')

        self.assertIsNone(p.match('Well,'))
        self.assertIsNone(p.match('well,'))
        self.assertIsNone(p.match('well.'))

    def test_colon(self):
        p = re.compile('(?=[^A-Z])[^0-9,\.]{5,}')

        self.assertIsNone(p.match('jobs:'))

if __name__ == '__main__':
    unittest.main()
