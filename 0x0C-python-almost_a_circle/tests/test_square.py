"""
This file contains test cases for square.py
"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class.
    """

    def test_area(self):
        """
        Test the area method of Rectangle.
        """
        r1 = Rectangle(5, 10)
        self.assertEqual(r1.area(), 50)
        
        r2 = Rectangle(2, 8)
        self.assertEqual(r2.area(), 16)

    def test_display(self):
        """
        Test the display method of Rectangle.
        """
        r1 = Rectangle(3, 2)
        expected_output = "###\n###\n"
        self.assertEqual(self.capture_stdout(r1.display), expected_output)
        
        r2 = Rectangle(2, 4, 1, 1)
        expected_output = "\n ##\n ##\n"
        self.assertEqual(self.capture_stdout(r2.display), expected_output)

    def test_str(self):
        """
        Test the __str__ method of Rectangle.
        """
        r1 = Rectangle(4, 6, 2, 1, 12)
        expected_output = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(r1), expected_output)

        r2 = Rectangle(5, 5, 1)
        expected_output = "[Rectangle] (1) 1/0 - 5/5"
        self.assertEqual(str(r2), expected_output)

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
