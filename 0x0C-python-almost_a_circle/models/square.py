#!/usr/bin/python3

"""
Module contains the Square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class, inherits from Rectangle.

    Attributes:
        size (int): The size of the square.
        x (int): The x-coordinate of the square's position.
        y (int): The y-coordinate of the square's position.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square's position.
                Defaults to 0.
            y (int, optional): The y-coordinate of the square's position.
                Defaults to 0.
            id (int, optional): The object's identifier. Defaults to None.

        Returns:
            None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the Square instance.

        Returns:
            str: The string representation of the Square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Square.

        Returns:
            dict: The dictionary representation of the Square.
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
