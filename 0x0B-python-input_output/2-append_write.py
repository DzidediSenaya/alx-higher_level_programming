#!/usr/bin/python3

"""
Module contains append_write function
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)
    Return: the number of characters added
    """
    try:
        with open(filename, 'a+', encoding='utf-8') as file:
            file.seek(0, 2)
            file.write(text)
            return len(text)
    except OSError:
        return 0
