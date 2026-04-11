#!/usr/bin/env python3
"""
Module for VerboseList class that extends the built-in list.
"""


class VerboseList(list):
    """
    A custom list class that prints notifications when modified.
    """

    def append(self, item):
        """Adds an item and prints a message."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """Extends the list and prints a message with the count of items."""
        count = len(x)
        super().extend(x)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """Prints a message and removes an item."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Prints a message and pops an item."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
