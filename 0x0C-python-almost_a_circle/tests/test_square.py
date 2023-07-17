#!/usr/bin/python3
"""
This file contains test cases for square.py
"""


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Test cases for the Square class.
    """

    def test_area(self):
        """
        Test the area method of Square.
        """
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)
        
        s2 = Square(8)
        self.assertEqual(s2.area(), 64)

    def test_display(self):
        """
        Test the display method of Square.
        """
        s1 = Square(3)
        expected_output = "###\n###\n###\n"
        self.assertEqual(self.capture_stdout(s1.display), expected_output)
        
        s2 = Square(4, 1, 1)
        expected_output = "\n ###\n ###\n ###\n"
        self.assertEqual(self.capture_stdout(s2.display), expected_output)

    def test_str(self):
        """
        Test the __str__ method of Square.
        """
        s1 = Square(4, 2, 1, 12)
        expected_output = "[Square] (12) 2/1 - 4"
        self.assertEqual(str(s1), expected_output)

        s2 = Square(5, 1, 0)
        expected_output = "[Square] (1) 1/0 - 5"
        self.assertEqual(str(s2), expected_output)

    def capture_stdout(self, func):
        """
        Helper method to capture stdout output.
        """
        import io
        from contextlib import redirect_stdout

        output = io.StringIO()
        with redirect_stdout(output):
            func()
        return output.getvalue()


if __name__ == '__main__':
    unittest.main()
