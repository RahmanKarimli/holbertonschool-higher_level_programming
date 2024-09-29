#!/usr/bin/python3
"""class"""


class CountedIterator:
    """class"""
    def __init__(self, data):
        self.data = iter(data)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __next__(self):
        try:
            item = next(self.data)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration
