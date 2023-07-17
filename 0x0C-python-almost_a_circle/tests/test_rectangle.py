"""
Test cases for the Rectangle class.

This file contains unit tests for the methods and
functionalities of the Rectangle class
defined in the 'rectangle.py' module.
"""


import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_area(self):
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

    def test_display(self):
        rect = Rectangle(4, 3)
        expected_output = "####\n####\n####\n"
        with patch("sys.stdout", new=StringIO()) as fake_output:
            rect.display()
            self.assertEqual(fake_output.getvalue(), expected_output)

    def test_str(self):
        rect = Rectangle(2, 4, 1, 1, 1)
        expected_output = "[Rectangle] (1) 1/1 - 2/4"
        self.assertEqual(str(rect), expected_output)

    def test_update(self):
        rect = Rectangle(5, 5)
        rect.update(1, 2, 3, 4, 5)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 5)

if __name__ == '__main__':
    unittest.main()
