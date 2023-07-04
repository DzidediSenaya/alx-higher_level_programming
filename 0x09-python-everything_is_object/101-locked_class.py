#!/usr/bin/python3
"""Defines a locked class."""
class LockedClass:
    """
    Restricts user from dynamically creating  new instance attributes
    except for 'first_name'
    """
    __slots__ = ['first_name']
