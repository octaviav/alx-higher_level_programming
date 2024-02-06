#!/usr/bin/python3
"""Defines a function that appends a file."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.

    Args:
        filename (str): Name of the file to append to.
        text (str): String to append to the file.
    Returns:
        The total number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
