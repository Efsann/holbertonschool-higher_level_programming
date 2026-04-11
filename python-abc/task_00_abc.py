#!/usr/bin/env python3
"""
Module for Animal abstract base class and its subclasses.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class Animal
    """
    @abstractmethod
    def sound(self):
        """
        Abstract method sound
        """
        pass


class Dog(Animal):
    """
    Class Dog that inherits from Animal
    """
    def sound(self):
        """
        Implementation of sound for Dog
        """
        return "Bark"


class Cat(Animal):
    """
    Class Cat that inherits from Animal
    """
    def sound(self):
        """
        Implementation of sound for Cat
        """
        return "Meow"
