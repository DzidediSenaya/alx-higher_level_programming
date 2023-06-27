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
        Initializes an instance of the Square class

        Args:
            size (int): The size of the square (default: 0)
        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieves the size of the square

        Returns:
            int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square

        Args:
            value (int): The new size of the square
        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Computes and returns the area of the square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2
