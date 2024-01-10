#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if search == k else k for k in my_list]
