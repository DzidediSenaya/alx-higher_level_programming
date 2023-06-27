#!/usr/bin/python3
"""
This module contains the Square class
"""


class Square:
    """
    Represents a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square

        Args:
            size (int): The size of the square (default: 0)
            position (tuple): The position of the square (default: (0, 0))
        Raises:
            TypeError: If size is not an integer
                      If position is not a tuple of 2 positive integers
            ValueError: If size is less than 0
        """
        self.size = size
        self.position = position

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
            value (int): The new size for the square
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

    @property
    def position(self):
        """
        Retrieves the position of the square

        Returns:
            tuple: The position of the square as a tuple of 2 positive integers
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square

        Args:
            value (tuple): The new position for the square
        Raises:
            TypeError: If position is not a tuple
                      If position tuple does not contain 2 integers
            ValueError: If position tuple does not contain 2 positive integers
        """
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(num, int) for num in value) or any(num < 0 for num in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates the area of the square

        Returns:
            int: The area of the square
        """
        return self.size ** 2

    def my_print(self):
        """
        Prints the square using '#'
        """
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """
        Returns a string representation of the square

        Returns:
            str: The string representation of the square
        """
        string_repr = ""
        if self.size == 0:
            string_repr += "\n"
        else:
            for _ in range(self.position[1]):
                string_repr += "\n"
            for _ in range(self.size):
                string_repr += " " * self.position[0] + "#" * self.size + "\n"
        return string_repr.rstrip()
