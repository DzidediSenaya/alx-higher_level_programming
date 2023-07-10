#!/usr/bin/python3
"""
This module contains a square class and init function
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
        __init__(self, width, height): Initializes a rectangle with the
        given width and height.
        area(self): Calculates and returns the area of the rectangle.
        __str__(self): Returns the string representation of the
        rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a rectangle with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is not a positive
            integer.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """
    Represents a square.

    Inherits from Rectangle.

    Public Methods:
        __init__(self, size): Initializes a square with the
        given size.
    """

    def __init__(self, size):
        """
        Initializes a square with the given size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not positive.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Returns the string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"
