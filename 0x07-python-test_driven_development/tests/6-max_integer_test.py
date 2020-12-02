#!/usr/bin/python3
""" Unittest for max_integer([..]) """
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Test for max integers """

    def test_cases(self):
        """ Different cases """
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([4, 6, 2, 10, 1]), 10)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([-3, -15, -67, -5, -9]), -3)
        self.assertEqual(max_integer([-3, -15, 67, -5, -9]), 67)
        self.assertEqual(max_integer([[4], [67], [10], [12]]), [67])
        self.assertEqual(max_integer([2.3, 5.6, 1.2, 10.4]), 10.4)
        self.assertEqual(max_integer([0, 0, 0]), 0)
        self.assertEqual(max_integer([8]), 8)

if __name__ == '__main__':
    unittest.main()
