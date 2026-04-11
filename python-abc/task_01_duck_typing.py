#!/usr/bin/env python3
"""
Module for Shape, Circle, Rectangle and shape_info function.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class for a shape."""

    @abstractmethod
    def area(self):
        """Method to calculate area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Method to calculate perimeter."""
        pass


class Circle(Shape):
    """Circle class that inherits from Shape."""

    def __init__(self, radius):
        """Initialize Circle with radius."""
        self.radius = radius

    def area(self):
        """Calculate area using radius."""
        return math.pi * (abs(self.radius) ** 2)

    def perimeter(self):
        """Calculate perimeter using radius."""
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """Rectangle class that inherits from Shape."""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate area."""
        return abs(self.width * self.height)

    def perimeter(self):
        """Calculate perimeter."""
        return 2 * (abs(self.width) + abs(self.height))


def shape_info(shape):
    """Function that prints area and perimeter of a shape."""
    area = shape.area()
    perimeter = shape.perimeter()
    print("Area: {}".format(area))
    print("Perimeter: {}".format(perimeter))
