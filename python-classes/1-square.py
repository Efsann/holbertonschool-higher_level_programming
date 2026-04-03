#!/usr/bin/python3
"""This module defines a class Square with a private attribute size."""


class Square:
    """A class that defines a square."""

    def __init__(self, size):
        """Initialize the square.

        Args:
            size: The size of the square (no type/value checking yet).
        """
        self.__size = size
