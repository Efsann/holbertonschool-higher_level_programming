#!/usr/bin/env python3
"""
Module defining Shape, Circle, Rectangle and shape_info
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class Shape"""

    @abstractmethod
    def area(self):
        """Abstract method for area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method for perimeter"""
        pass


class Circle(Shape):
    """Circle class implementation"""

    def __init__(self, radius):
        """Constructor for Circle"""
        self.radius = radius

    def area(self):
        """Returns circle area"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Returns circle perimeter"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class implementation"""

    def __init__(self, width, height):
        """Constructor for Rectangle"""
        self.width = width
        self.height = height

    def area(self):
        """Returns rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """Returns rectangle perimeter"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints shape area and perimeter using duck typing"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
