#!/usr/bin/python3
import math


class MagicClass:
    """A class that represents a magic circle."""

    def __init__(self, radius=0):
        """
        Initialize a MagicClass instance.

        Args:
            radius (float or int): The radius of the magic circle.

        Raises:
            TypeError: If radius is not a number.
        """
        self._MagicClass__radius = 0  # Name mangling to match the bytecode
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self._MagicClass__radius = radius

    def area(self):
        """
        Calculate the area of the magic circle.

        Returns:
            float: The area of the magic circle.
        """
        return 2 * math.pi * self._MagicClass__radius ** 2

    def circumference(self):
        """
        Calculate the circumference of the magic circle.

        Returns:
            float: The circumference of the magic circle.
        """
        return 2 * math.pi * self._MagicClass__radius
