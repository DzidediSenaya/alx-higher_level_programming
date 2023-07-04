#!/usr/bin/python3
"""
Module for text indentation
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines after each '.', '?' or ':'

    Args:
        text (str): Input text

    Returns:
        None

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = (".", "?", ":")

    for separator in separators:
        text = text.replace(separator, separator + "\n\n")

    lines = [line.strip() for line in text.split("\n")]

    formatted_text = "\n".join(lines)
    print(formatted_text)
