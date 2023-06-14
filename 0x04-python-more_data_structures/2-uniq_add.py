#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for item in my_list:
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)
    return new_list


def uniq_add(my_list=[]):
    unique_integers = set()
    for num in my_list:
        unique_integers.add(num)
    sum_unique_integers = sum(unique_integers)
    return sum_unique_integers
