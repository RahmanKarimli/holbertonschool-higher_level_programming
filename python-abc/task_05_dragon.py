#!/usr/bin/python3
"""class"""


class FlyMixin:
    """class"""
    def fly(self):
        print("The creature flies!")


class SwimMixin:
    """class"""
    def swim(self):
        print("The creature swims!")


class Dragon(SwimMixin, FlyMixin):
    """class"""
    def roar(self):
        print("The dragon roars!")
