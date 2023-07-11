#!/usr/bin/python3

"""
Module contains the write_file function
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8)
    Return: the number of characters written
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)
            return len(text)
    except OSError:
        return 0
