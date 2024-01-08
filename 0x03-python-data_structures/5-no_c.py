#!/usr/bin/python3
def no_c(my_string):
    if my_string[:]:
        string_new = my_string.translate({ord("c"): None})
        second_string = string_new.translate({ord("C"): None})
        return second_string
    return my_string
