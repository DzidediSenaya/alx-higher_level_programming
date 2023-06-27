#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        while count < x:
            print("{:d}".format(my_list[count]), end=" ")
            count += 1
    except IndexError:
        pass
    finally:
        print()
    return count


safe_print_list = __import__('0-safe_print_list').safe_print_list

value = [89]
nb_print = safe_print_list(value, len(value) + 2)
print("Number of integers printed: {:d}".format(nb_print))
