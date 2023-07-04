#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)
        self.assertEqual(max_integer([-1, -1, -1, -1]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 0, 1]), 1)
        self.assertEqual(max_integer([-1, 0, 1, 0, -1]), 1)
        self.assertEqual(max_integer([-1, -1, 0, 0, 1, 1]), 1)

    def test_single_element_list(self):
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-5]), -5)

    def test_large_numbers(self):
        self.assertEqual(max_integer([999999, -999999]), 999999)
        self.assertEqual(max_integer([10**9, -(10**9)]), 10**9)

if __name__ == '__main__':
    unittest.main()

