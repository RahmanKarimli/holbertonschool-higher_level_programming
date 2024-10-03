#!/usr/bin/python3
"""python"""


def append_write(filename="", text=""):
    """function"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
