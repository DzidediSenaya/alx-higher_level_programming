#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            result = 0
            if i < len(my_list_1) and i < len(my_list_2):
                if isinstance(my_list_1[i], (int, float)):
                    if isinstance(my_list_2[i], (int, float)):
                        if my_list_2[i] != 0:
                            result = my_list_1[i] / my_list_2[i]
                        else:
                            raise ZeroDivisionError
                    else:
                        raise TypeError
                else:
                    raise TypeError
            else:
                raise IndexError
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return new_list
