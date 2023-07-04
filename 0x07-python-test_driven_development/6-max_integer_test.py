#!/usr/bin/python3
"""
Unittest for max_integer function
"""
import unittest
from max_integer import max_integer


class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_sorted_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_reversed_list(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_duplicate_values(self):
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_float_values(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

    def test_mixed_values(self):
        self.assertEqual(max_integer([-1, 2.2, 3, -4]), 3)


if __name__ == '__main__':
    unittest.main()
