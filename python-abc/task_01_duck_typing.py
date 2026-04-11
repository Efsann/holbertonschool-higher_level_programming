#!/usr/bin/env python3
"""
Module for Shape, Circle, Rectangle and shape_info
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
    """Class Circle"""
    def __init__(self, radius):
        """Initializes Circle"""
        self.__radius = radius

    def area(self):
        """Calculates area"""
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        """Calculates perimeter"""
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """Class Rectangle"""
    def __init__(self, width, height):
        """Initializes Rectangle"""
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates area"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates perimeter"""
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """Prints area and perimeter"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
