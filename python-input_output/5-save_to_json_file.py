#!/usr/bin/python3
"""python"""
import json


def save_to_json_file(my_obj, filename):
    """function"""
    with open(file=filename, mode="w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
