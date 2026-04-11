#!/usr/bin/env python3
"""
Module for Animal abstract base class and its subclasses Dog and Cat.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class representing an Animal."""

    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by subclasses."""
        pass


class Dog(Animal):
    """Class representing a Dog, inheriting from Animal."""

    def sound(self):
        """Returns the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Class representing a Cat, inheriting from Animal."""

    def sound(self):
        """Returns the sound of a cat."""
        return "Meow"
