#!/usr/bin/python3
"""Module containing Student class"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            dick = {}
            for i in attrs:
                if i in self.__dict__:
                    dick[i] = self.__dict__[i]
            return dick
        return self.__dict__

    def reload_from_json(self, json):
        for i in self.__dict__.keys():
            for j in json.keys():
                if i == j:
                    self.__dict__[i] = json[j]
