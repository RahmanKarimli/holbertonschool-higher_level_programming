#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 3-square.py)"""


class Square:
    """instance attribute: size"""
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

        if (position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if (self.__size == 0):
            print()
        else:
            line = self.__position[1]
            for i in range(self.__size):
                space = self.__position[0]
                if (line > 0):
                    print()
                    line -= 1
                for j in range(self.__size + space):
                    if (space > 0):
                        print(" ", end="")
                        space -= 1
                        continue
                    print("#", end="")
                print()
