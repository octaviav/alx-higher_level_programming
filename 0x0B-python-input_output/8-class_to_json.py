#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """The dictionary represntation of a simple data structure is returned."""
    return obj.__dict__
