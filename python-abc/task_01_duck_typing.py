#!/usr/bin/env python3
"""
Module defining Shape, Circle, Rectangle and shape_info
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes"""

    @abstractmethod
    def area(self):
        """Abstract method for area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method for perimeter"""
        pass


class Circle(Shape):
    """Circle class"""

    def __init__(self, radius):
        """Initialize Circle"""
        self.radius = radius

    def area(self):
        """Calculate area of circle"""
        return math.pi * (abs(self.radius) ** 2)

    def perimeter(self):
        """Calculate perimeter of circle"""
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """Rectangle class"""

    def __init__(self, width, height):
        """Initialize Rectangle"""
        self.width = width
        self.height = height

    def area(self):
        """Calculate area of rectangle"""
        return abs(self.width) * abs(self.height)

    def perimeter(self):
        """Calculate perimeter of rectangle"""
        return 2 * (abs(self.width) + abs(self.height))


def shape_info(shape):
    """Print area and perimeter using duck typing"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
 
