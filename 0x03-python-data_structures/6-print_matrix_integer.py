#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for k in matrix:
            for j in k:
                print("{:d}".format(j), end=' ' if j != k[-1] else '')
            print()
