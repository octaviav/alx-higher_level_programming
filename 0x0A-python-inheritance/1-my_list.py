#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements sorted built-in list class for printing."""

    def print_sorted(self):
        """Prints a list in ascending order."""
        print(sorted(self))
