#!/usr/bin/python3
"""Function to add 2 nums"""


def add_integer(a, b=98):
    """
    function that adds 2 numbers
    """
    lst = [int, float]

    if (type(a) not in lst):
        raise TypeError("a must be an integer")
    if (type(b) not in lst):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
