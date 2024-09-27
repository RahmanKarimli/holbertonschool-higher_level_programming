#!/usr/bin/python3
"""class"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """class"""
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """Dog class Inherited from Animal"""
    def sound(self):
        return "Bark"

class Cat(Animal):
    """Cat class Inherited from Animal"""
    def sound(self):
        return "Meow"
