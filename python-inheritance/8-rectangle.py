#!/usr/bin/python3
"""class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        BaseGeometry.integer_validator("width", width)
        self.__width = width
        BaseGeometry.integer_validator("height", height)
        self.__height = height
