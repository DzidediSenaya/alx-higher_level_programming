#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Get the sorted list of keys in the dictionary
    sorted_keys = sorted(a_dictionary.keys())

    # Iterate over the sorted keys and print each key-value pair
    for key in sorted_keys:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
