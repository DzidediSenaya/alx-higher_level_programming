#!/usr/bin/python3
"""
This module contains a rectangle class
"""


class Rectangle:
    """
    Represents a rectangle.

    Inherits from BaseGeometry.

    Public Methods:
        __init__(self, width, height): Initializes a rectangle with the
        given width and height.
    """

    def __init__(self, width, height):
        """
        Initializes a rectangle with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is not a positive integer.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
