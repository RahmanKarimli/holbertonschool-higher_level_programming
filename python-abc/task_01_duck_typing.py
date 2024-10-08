#!/usr/bin/python3
"""class"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """class"""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    """class"""
    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return pi * self.radius * 2

class Rectangle(Shape):
    """Class"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

def shape_info(cls):
    area = cls.area()
    perimeter = cls.perimeter()

    # Printing the area and perimeter
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
