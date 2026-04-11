#!/usr/bin/env python3
"""
Shapes module for duck typing and ABC.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class for Shape."""

    @abstractmethod
    def area(self):
        """Abstract method for area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method for perimeter."""
        pass


class Circle(Shape):
    """Circle class implementation."""

    def __init__(self, radius):
        """Initialize Circle with radius."""
        self.radius = radius

    def area(self):
        """Calculate area of the circle."""
        return math.pi * (abs(self.radius) ** 2)

    def perimeter(self):
        """Calculate perimeter of the circle."""
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """Rectangle class implementation."""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate area of the rectangle."""
        return abs(self.width * self.height)

    def perimeter(self):
        """Calculate perimeter of the rectangle."""
        return 2 * (abs(self.width) + abs(self.height))


def shape_info(shape):
    """Function to print area and perimeter using duck typing."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
