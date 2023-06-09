#!/usr/bin/python3
"""Defines a rectangle Class """


class Rectangle:
    """
    A class representing a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        number_of_instances (int): The number of rectangle instances created.

    Methods:
        __init__(width=0, height=0): Initialize a Rectangle object.
        area(): Calculate the area of the rectangle.
        perimeter(): Calculate the perimeter of the rectangle.
        __str__(): Return a string representation of the rectangle.
        __repr__(): Return a string representation that can be used
        to recreate the rectangle.
        __del__(): Clean up resources when the rectangle object is deleted.

    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle object with the given width and height.

        Args:
            width (int): The width of the rectangle (default: 0).
            height (int): The height of the rectangle (default: 0).

        Raises:
            TypeError: If the width or height is not an integer.
            ValueError: If the width or height is less than 0.

        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.

        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.

        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.

        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.

        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle.

        """
        if self.width == 0 or self.height == 0:
            return ""
        rect_str = ""
        for _ in range(self.height):
            rect_str += "#" * self.width + "\n"
        return rect_str.rstrip()

    def __repr__(self):
        """
        Return a string representation that can be used to recreate
        the rectangle.

        Returns:
            str: A string representation of the rectangle.

        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Clean up resources when the rectangle object is deleted.

        This method is called when the rectangle object is no longer
        referenced.

        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
