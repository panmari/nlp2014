
import unittest
from ex5.my_dictionary import MyDictionary

class MyTestCase(unittest.TestCase):

    def test_add_and_retrieve_single_letter(self):
        d = MyDictionary()
        d.insert('a')
        self.assertEqual('a', d.lookUp('a'))

    def test_add_same_letter_twice_should_error(self):
        d = MyDictionary()
        d.insert('a')
        with self.assertRaises(KeyError):
            d.insert('a')

    def test_add_and_remove_and_retrieve_single_letter(self):
        d = MyDictionary()
        d.insert('a')
        d.remove('a')
        self.assertEqual(None, d.lookUp('a'))

    def test_add_and_retrieve_multiple_letters(self):
        d = MyDictionary()
        d.insert('a')
        d.insert('b')
        d.insert('c')
        self.assertEqual('a', d.lookUp('a'))
        self.assertEqual('b', d.lookUp('b'))
        self.assertEqual('c', d.lookUp('c'))

    def test_resize(self):
        d = MyDictionary(100)
        # insert a, aa, aaa, etc..
        for i in range(72, 72+100):
            d.insert(chr(i))
        self.assertEqual('H', d.lookUp('H'))
        self.assertEqual('J', d.lookUp('J'))
        self.assertEqual(100, d.entries)
        self.assertTrue(d.size() > 50)
        self.assertEqual(200, d.capacity)
        print(d.d)

if __name__ == '__main__':
    unittest.main()
