#!/usr/bin/python3
"""Module for checking exact class instances."""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of a given class.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        True if exactly an instance, otherwise False.
    """
    return type(obj) is a_class
