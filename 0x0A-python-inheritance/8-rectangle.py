#!/usr/bin/python3
"""
This module contains a rectangle class and init function
"""


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.

    Inherits from BaseGeometry.

    Public Methods:
        __init__(self, width, height): Initializes a
    rectangle with the given width and height.

    Private Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a rectangle with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If either width or height is not an integer.
            ValueError: If either width or height is not positive.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
