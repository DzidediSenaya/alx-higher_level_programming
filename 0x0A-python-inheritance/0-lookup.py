#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attributes and methods
    of an object.

    Args:
        obj: The object to look up.

    Returns:
        A list of strings representing the attributes and
        methods of the object.
    """
    return dir(obj)


class MyClass1(object):
    """
    This is MyClass1.
    """


class MyClass2(object):
    """
    This is MyClass2.
    """
    my_attr1 = 3

    def my_meth(self):
        """
        This is my_meth.
        """
        pass
