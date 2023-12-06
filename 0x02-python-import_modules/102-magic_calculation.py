#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)

        for my_num in range(4, 6):
            c =  add(c, my_num)
        return(c)
    else:
        return sub(a, b)