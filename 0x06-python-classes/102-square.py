#!/usr/bin/python3
"""
This module contains the Square class
"""


class Square:
    """
    Represents a square
    """
    def __init__(self, size=0):
        """
        Initializes a square

        Args:
            size (int): The size of the square (default: 0)
        Raises:
            TypeError: If size is not a number
            ValueError: If size is less than 0
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square

        Returns:
            float: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square

        Args:
            value (float): The new size for the square
        Raises:
            TypeError: If size is not a number
            ValueError: If size is less than 0
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square

        Returns:
            float: The area of the square
        """
        return self.size ** 2

    def __eq__(self, other):
        """
        Equality operator for comparing two squares based on their area

        Args:
            other (Square): The other square to compare with
        Returns:
            bool: True if the squares have equal areas, False otherwise
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Inequality operator for comparing two squares based on their area

        Args:
            other (Square): The other square to compare with
        Returns:
            bool: True if the squares have different areas, False otherwise
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Greater than operator for comparing two squares based on their area

        Args:
            other (Square): The other square to compare with
        Returns:
            bool: True if the area of the first square is greater than the second square, False otherwise
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Greater than or equal to operator for comparing two squares based on their area

        Args:
            other (Square): The other square to compare with
        Returns:
            bool: True if the area of the first square is greater than or equal to the second square, False otherwise
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Less than operator for comparing two squares based on their area

        Args:
            other (Square): The other square to compare with
        Returns:
            bool: True if the area of the first square is less than the second square, False otherwise
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Less than or equal to operator for comparing two squares based on their area

        Args:
            other (Square): The other square to compare with
        Returns:
            bool: True if the area of the first square is less than or equal to the second square, False otherwise
        """
        return self.area() <= other.area()
