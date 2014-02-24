
import unittest
from ex1.my_complex import MyComplex

class MyTestCase(unittest.TestCase):
    def test_add(self):
        a = MyComplex(1, 1)
        b = MyComplex(2, 2)
        self.assertEqual(MyComplex(3,3), a + b)

    def test_sub(self):
        a = MyComplex(1, 1)
        b = MyComplex(2, 2)
        self.assertEqual(MyComplex(-1,-1), a - b)

    def test_add_sub(self):
        a = MyComplex(1, 1)
        b = MyComplex(2, 2)
        self.assertEqual((MyComplex(3,3), MyComplex(-1,-1)), a.addSub(b))

    def test_string_conversion(self):
        a = MyComplex(2, 2)
        self.assertEqual("2*i + 2", str(a))

if __name__ == '__main__':
    unittest.main()
