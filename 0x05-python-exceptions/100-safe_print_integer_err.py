#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        error_message = "Exception: {}".format(e)
        print(error_message, file=sys.stderr)
        return False


safe_print_integer_err = __import__('100-safe_print_integer_err').safe_print_integer_err

value = [89]
print(safe_print_integer_err(value))

safe_print_integer_err = __import__('100-safe_print_integer_err').safe_print_integer_err

value = None
print(safe_print_integer_err(value))
