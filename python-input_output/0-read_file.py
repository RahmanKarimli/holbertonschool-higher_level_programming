#!/usr/bin/python3
"""Module containing read_file function"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        print(f.read())
