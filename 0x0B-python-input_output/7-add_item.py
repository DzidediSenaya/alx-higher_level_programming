#!/usr/bin/python3

"""
Module contains functions to save and load Python
objects as JSON files.
"""

import sys
from typing import Any
from json import dump, load


def save_to_json_file(my_obj: Any, filename: str) -> None:
    """
    Writes a Python object to a JSON file.

    Args:
        my_obj (Any): The object to be saved as JSON.
        filename (str): The name of the file to save the JSON
        data.

    Returns:
        None
    """
    with open(filename, 'w') as file:
        dump(my_obj, file)


def load_from_json_file(filename: str) -> Any:
    """
    Loads a JSON file and returns the corresponding Python object.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        Any: The Python object loaded from the JSON file.
    """
    with open(filename) as file:
        return load(file)


def main() -> None:
    """
    Entry point of the script.
    Reads command-line arguments, adds them to a Python list,
    and saves the list as JSON in a file.
    """
    filename = "add_item.json"

    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        my_list = []

    my_list.extend(sys.argv[1:])

    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    main()
