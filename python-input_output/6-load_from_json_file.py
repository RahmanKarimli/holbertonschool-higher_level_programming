#!/usr/bin/python3
"""python"""
import json


def load_from_json_file(filename):
    """function"""
    with open(filename, mode="r", encoding="utf-8") as f:
        data = f.read()

    return json.loads(data)
