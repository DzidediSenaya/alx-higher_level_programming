#!/usr/bin/python3
"""
Contains a student class and three
functions
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
         Returns:
            dict: A dictionary representation of the
            student's attributes.
        """
        if attrs is None:
            attrs = self.__dict__.keys()

        json_dict = {
            attr: getattr(self, attr)
            for attr in attrs
            if hasattr(self, attr)
        }

        return json_dict

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance
        based on the provided dictionary.
        """
        for attr, value in json.items():
            setattr(self, attr, value)
