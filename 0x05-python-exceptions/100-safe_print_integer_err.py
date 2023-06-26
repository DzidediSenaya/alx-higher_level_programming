#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except:
        error_message = "Exception: Unknown format code 'd' for object of type '{}'"
        error_message = error_message.format(value.__class__.__name__)
        print(error_message, file=sys.stderr)
        return False
