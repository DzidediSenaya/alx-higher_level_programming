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
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Computes and returns the area of the square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2
