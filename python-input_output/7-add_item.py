#!/usr/bin/python3
"""Module for adding arguments to a Python list"""
from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    new = load_from_json_file("add_item.json")
except FileNotFoundError:
    new = []
new.extend(argv[1:])
save_to_json_file(new, "add_item.json")
