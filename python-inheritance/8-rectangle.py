#!/usr/bin/python3
"""class"""


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        BaseGeometry.integer_validator("width", width)
        self.__width = width
        BaseGeometry.integer_validator("height", height)
        self.__height = height
