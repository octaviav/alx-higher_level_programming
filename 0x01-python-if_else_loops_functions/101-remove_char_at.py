#!/usr/bin/python3
def remove_char_at(str, n):
    rm = ''
    k = 0
    for char in str:
        if k != n:
            rm += str[k]
        k += 1
    return (rm)
