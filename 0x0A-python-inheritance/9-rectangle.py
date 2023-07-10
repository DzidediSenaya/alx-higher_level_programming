#!/usr/bin/python3
"""
This module contains a rectangle class and _init_ function
"""


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.

    Inherits from BaseGeometry.

    Public Methods:
        __init__(self, width, height): Initializes a rectangle
        with the given width and height.
        area(self): Calculates and returns the area of the rectangle.

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

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return the string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
