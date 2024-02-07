#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represents Pascal's Triangle of size n.

    Returns lists of integers representing the triangle in a list.
    """
    if n <= 0:
        return []

    trias = [[1]]
    while len(trias) != n:
        tri = trias[-1]
        tmp = [1]
        for k in range(len(tri) - 1):
            tmp.append(tri[k] + tri[k + 1])
        tmp.append(1)
        trias.append(tmp)
    return trias
