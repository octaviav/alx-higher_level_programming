#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.

    Args:
        my_list (list): List to print elements from.
        x (int): Number of elements in my_list to print.

    Returns:
        The number of elements printed.
    """
    nom = 0
    for k in range(x):
        try:
            print("{}".format(my_list[k]), end="")
            nom += 1
        except IndexError:
            break
    print("")
    return (nom)
