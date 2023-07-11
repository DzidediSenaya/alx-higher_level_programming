#!/usr/bin/python3

"""
This module contains a class definition
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

    def to_json(self):
        """
        Return a dictionary representation of the Student
        instance.

        Returns:
            dict: A dictionary representation of the
            student's attributes.
        """
        json_dict = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
        return json_dict
