#!/usr/bin/python3
"""class"""


class VerboseList(list):
    """class"""
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, x):
        super().extend(x)
        print(f"Extended the list with [{len(x)}] items.")

    def remove(self, item):
        if item in self:
            print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, item = None):
        if item is None:
            print(f"Popped [{super().pop()}] from the list.")
            return super().pop()
        else:
            item = super().pop(item)
            print(f"Popped [{item}] from the list.")
            return super().pop(item)
