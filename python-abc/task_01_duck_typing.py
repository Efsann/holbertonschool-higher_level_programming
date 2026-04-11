#!/usr/bin/env python3
"""
Module for Shape, Circle, Rectangle and shape_info function
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class Shape"""

    @abstractmethod
    def area(self):
        """Abstract method area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method perimeter"""
        pass


class Circle(Shape):
    """Class Circle that inherits from Shape"""

    def __init__(self, radius):
        """Initializes Circle with radius"""
        self.radius = radius

    def area(self):
        """Calculates area of circle"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculates perimeter of circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Class Rectangle that inherits from Shape"""

    def __init__(self, width, height):
        """Initializes Rectangle with width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Calculates area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Calculates perimeter of rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints the area and perimeter of a shape"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
