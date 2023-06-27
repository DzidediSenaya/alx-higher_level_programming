#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            if i < len(my_list) and isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
        print()
        return count
    except IndexError:
        print("Error: Index out of range.")
        return count


safe_print_list_integers = __import__('2-safe_print_list_integers').safe_print_list_integers

my_list = [1, 2, 3, 4]
x = len(my_list) + 4
nb_print = safe_print_list_integers(my_list, x)
print("{:d}".format(nb_print))
