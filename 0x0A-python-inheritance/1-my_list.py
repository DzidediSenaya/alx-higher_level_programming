#!/usr/bin/python3
"""
This module contains class MyList that inherits from list
"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.

    Public Methods:
        print_sorted(): Print the list in sorted (ascending) order.
    """
    def print_sorted(self):
        """
        Print the list in sorted (ascending) order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
