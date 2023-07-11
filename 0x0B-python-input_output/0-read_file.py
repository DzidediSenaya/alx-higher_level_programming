#!/usr/bin/python3

"""
Module contains read_file function
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            while True:
                line = file.readline()
                if not line:
                    break
                print(line, end='')
    except OSError:
        pass
