#!/usr/bin/python3
class Square(Rectangle):
    """
    A class representing a square.

    Inherits from Rectangle.

    Public Methods:
        __init__(self, size): Initializes a square
        with the given size.
        __str__(self): Returns a string representation
    of the square.
    """

    def __init__(self, size):
        """
        Initialize a square with the given size.

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
        Returns a string representation of the square.

        Returns:
            str: A string representation of the square in the
        format [Square] <width>/<height>.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
