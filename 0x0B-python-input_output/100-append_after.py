#!/usr/bin/python3
"""Defines a function that inserts a text file."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a given string in a file.

    Args:
        filename (str): Name of the file.
        search_string (str): String to find within the file.
        new_string (str): String to be inserted.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as w:
        w.write(txt)
