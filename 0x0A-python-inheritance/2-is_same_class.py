#!/usr/bin/python3
"""Defines a function that checks classes."""


def is_same_class(obj, a_class):
    """Checks whether the object is an instance of a class.

    Args:
        obj (any): Object to check.
        a_class (type): Class to match the type of obj to.
    Returns:
        If obj is an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
