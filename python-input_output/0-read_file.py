#!/usr/bin/python3
"""python"""


def read_file(filename=""):
    """functions"""
    with open(filename, encoding="utf-8") as f:
        read = f.read()
        print(read, end="")
