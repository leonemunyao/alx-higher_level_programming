#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for str_ing in my_string:
        if str_ing.lower() != 'c':
            new_string += str_ing
        return new_string