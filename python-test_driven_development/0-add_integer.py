#!/usr/bin/python3
"""Function to add 2 nums"""
def add_integer(a, b=98):
    """
    function that adds 2 numbers
    """
    try:
        a = int(a)
    except (ValueError, TypeError):
        raise TypeError("a must be an integer")
    try:
        b = int(b)
    except (ValueError, TypeError):
        raise TypeError("b must be an integer")
    return a + b
