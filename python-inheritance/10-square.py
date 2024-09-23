#!/usr/bin/python3
"""class"""
BaseGeometry = __import__('9-rectangle.py').BaseGeometry


class Square(Rectangle):
    """class"""
    def __init__(self, size):
        BaseGeometry.integer_validator(self, "size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2
