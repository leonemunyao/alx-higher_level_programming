#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(map(lambda j: replace if j == search else j, my_list))
    return (new_list)
