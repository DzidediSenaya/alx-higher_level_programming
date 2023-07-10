#!/usr/bin/python3
class MyInt(int):
    """
    A class representing a rebellious integer.

    Inherits from int.

    Public Methods:
        __eq__(self, other): Overrides the equality
        comparison operator (==).
        __ne__(self, other): Overrides the inequality
        comparison operator (!=).
    """

    def __eq__(self, other):
        """
        Overrides the equality comparison operator (==).

        Args:
            other: The value to compare with.

        Returns:
            bool: True if the values are not equal;
        False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the inequality comparison operator (!=).

        Args:
            other: The value to compare with.

        Returns:
            bool: True if the values are equal; False otherwise.
        """
        return super().__eq__(other)
