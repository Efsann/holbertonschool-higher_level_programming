#!/usr/bin/env python3
"""
Module defining Fish, Bird, and FlyingFish classes to demonstrate multiple inheritance.
"""


class Fish:
    """Class representing a fish."""

    def swim(self):
        """Prints a message about swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Prints a message about habitat."""
        print("The fish lives in water")


class Bird:
    """Class representing a bird."""

    def fly(self):
        """Prints a message about flying."""
        print("The bird is flying")

    def habitat(self):
        """Prints a message about habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Class representing a flying fish, inheriting from both Fish and Bird.
    """

    def fly(self):
        """Overrides the fly method from Bird."""
        print("The flying fish is soaring!")

    def swim(self):
        """Overrides the swim method from Fish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Overrides the habitat method from both parents."""
        print("The flying fish lives both in water and the sky!")
