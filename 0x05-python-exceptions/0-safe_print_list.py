#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nr = 0
    for k in range(x):
        try:
            print(my_list[k], end="")
            nr += 1
        except IndexError:
            break
        print("")
        return(x)
