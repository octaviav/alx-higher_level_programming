#!/usr/bin/python3
"""Defines a function that looks for objects."""


def lookup(obj):
    """Returns a list of an object's available attributes."""
    return (dir(obj))
