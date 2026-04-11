#!/usr/bin/env python3
"""
Module defining Mixins and a Dragon class to demonstrate behavior composition.
"""


class SwimMixin:
    """Mixin to add swimming behavior."""
    def swim(self):
        """Prints swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin to add flying behavior."""
    def fly(self):
        """Prints flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that inherits from SwimMixin and FlyMixin.
    Composes swimming and flying behaviors.
    """
    def roar(self):
        """Prints a roaring message unique to the dragon."""
        print("The dragon roars!")
