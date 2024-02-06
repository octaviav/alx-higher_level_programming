#!/usr/bin/python3
"""Defines a function that reads text in a file."""


def read_file(filename=""):
    """Prints out the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
