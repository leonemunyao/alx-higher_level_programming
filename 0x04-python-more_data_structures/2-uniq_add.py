#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = set(my_list)
    j = 0

    for k in unique_list:
        j += k

    return (j)
