#!/usr/bin/python3
"""
Module for checking class and subclass instances.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or if the object is an instance of
    a class that inherited from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        True if the object is an instance or subclass instance, else False.
    """
    return isinstance(obj, a_class)
