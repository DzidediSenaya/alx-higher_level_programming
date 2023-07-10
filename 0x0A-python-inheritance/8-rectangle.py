#!/usr/bin/python3
"""
This module contains a rectangle class
"""


class BaseGeometry:
    """
    A base class for geometry-related operations.
    """

    def integer_validator(self, name, value):
        """
        Validates that a value is an integer and greater than 0.

        Args:
            name (str): The name of the value.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Represents a rectangle.

    Inherits from BaseGeometry.

    Public Methods:
        __init__(self, width, height): Initializes a rectangle with the given width and height.
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
