#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for element in my_list:
            print(element, end="")
            count += 1
            if count >= x:
                break
        print()
        return count
    except TypeError:
        print("Error: Invalid element in the list.")
        return count


safe_print_list = __import__('0-safe_print_list').safe_print_list

my_list = [1, 2, 3, 4]
x = 0

nb_print = safe_print_list(my_list, x)
print("{:d}".format(nb_print))
