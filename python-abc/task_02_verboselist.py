#!/usr/bin/python3
"""VerboseList class extending list with additional functionality."""


class VerboseList(list):
    """A custom list that provides verbose output for common list operations."""

    def append(self, item):
        """Appends an item to the list and prints a message."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extends the list with elements from the iterable and prints a message."""
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """Removes an item from the list and prints a message if the item exists."""
        if item in self:
            super().remove(item)
            print(f"Removed [{item}] from the list.")
        else:
            raise ValueError(f"{item} not in list")

    def pop(self, index=None):
        """Removes and returns an item at the specified index or the last item, and prints a message."""
        if index is None:
            item = super().pop()
            print(f"Popped [{item}] from the list.")
            return item
        else:
            item = super().pop(index)
            print(f"Popped [{item}] from the list.")
            return item
