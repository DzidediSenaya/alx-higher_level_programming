#!/usr/bin/python3
"""
This module contains a base class and two functions
"""


class BaseGeometry:
    """
    A base class for geometry-related classes.

    Public Methods:
        area(self): Compute the area of the geometry.
        integer_validator(self, name, value):
        Validate an integer value.
    """

    def area(self):
        """
        Compute the area of the geometry.

        Raises:
            Exception: This method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate an integer value.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
