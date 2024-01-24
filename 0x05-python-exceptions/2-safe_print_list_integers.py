#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list that are integers.

    Args:
        my_list (list): List to print elements from.
        x (int): Number of elements of my_list to print.

    Returns:
        Number of elements printed.
    """
    nr = 0
    for k in range(0, x):
        try:
            print("{:d}".format(my_list[k]), end="")
            nr += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (nr)
