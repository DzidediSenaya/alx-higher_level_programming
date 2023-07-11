#!/usr/bin/python3

"""
Module contains a student class definition
and two functions
"""


class Student:
    """
    A class that defines a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance with first_name,
        last_name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the
        Student instance.
        """
        if attrs is None:
            attrs = self.__dict__.keys()

        json_dict = {
            attr: getattr(self, attr)
            for attr in attrs
            if hasattr(self, attr)
        }

        return json_dict
