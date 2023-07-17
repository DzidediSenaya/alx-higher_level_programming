#!/usr/bin/python3

"""
Module contains the Base class
"""

import turtle
import csv


class Base:
    """
    Base class for managing id attribute in all future classes.

    Attributes:
        __nb_objects (int): Private class attribute to track the
        number of objects created.
        id (int): Public instance attribute representing the
        object's unique identifier.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int, optional): The object's identifier. Defaults to None.

        Returns:
            None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to its JSON string representation.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """
        import json
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): List of instances that inherit from Base.

        Returns:
            None.
        """
        import json
        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs is not None:
            json_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as file:
            file.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON string representation to a list of dictionaries.

        Args:
            json_string (str): JSON string representing a list of dictionaries.

        Returns:
            list: List of dictionaries represented by json_string.
        """
        import json
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance with all attributes already set.

        Args:
            **dictionary: Dictionary containing the attributes.

        Returns:
            Instance with attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Create a dummy instance
        elif cls.__name__ == "Square":
            dummy = cls(1)  # Create a dummy instance
        dummy.update(**dictionary)   # use real values
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Loads a list of instances from a JSON file.

        Returns:
            List of instances.
        """
        import os.path
        import json
        filename = cls.__name__ + ".json"
        if not os.path.isfile(filename):
            return []
        with open(filename, "r") as file:
            json_string = file.read()
        json_list = cls.from_json_string(json_string)
        return [cls.create(**dictionary) for dictionary in json_list]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes list_objs to CSV format and saves it to a file.

        Args:
            list_objs (list): List of instances that inherit from Base.

        Returns:
            None.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as file:
            writer = csv.writer(file)
            if list_objs is not None and len(list_objs) > 0:
                if cls.__name__ == "Rectangle":
                    attributes = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    attributes = ["id", "size", "x", "y"]
                writer.writerow(attributes)
                for obj in list_objs:
                    values = [getattr(obj, attr) for attr in attributes]
                    writer.writerow(values)

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes instances from a CSV file and returns
        a list of instances.

        Returns:
            List of instances.
        """
        filename = cls.__name__ + ".csv"
        instances = []
        with open(filename, "r") as file:
            reader = csv.reader(file)
            attributes = next(reader)
            for row in reader:
                values = [int(value) for value in row]
                instance = cls.create(**dict(zip(attributes, values)))
                instances.append(instance)
        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Opens a window and draws all the Rectangles and Squares.

        Args:
            list_rectangles (list): List of Rectangle instances.
            list_squares (list): List of Square instances.

        Returns:
            None.
        """
        screen = turtle.Screen()
        turtle.speed(2)
        for rect in list_rectangles:
            turtle.penup()
            turtle.goto(rect.x, rect.y)
            turtle.pendown()
            for _ in range(2):
                turtle.forward(rect.width)
                turtle.right(90)
                turtle.forward(rect.height)
                turtle.right(90)
        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.right(90)
        turtle.done()
