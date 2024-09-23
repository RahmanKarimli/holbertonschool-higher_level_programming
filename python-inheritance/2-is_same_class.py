#!/usr/bin/python3
"""function"""


def is_same_class(obj, a_class):
    """function"""
    if obj.__class__ == a_class or a_class == object:
        return True
    return False
