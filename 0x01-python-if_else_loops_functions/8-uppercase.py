#!/usr/bin/python3

def uppercase(str):
    for my_letter in str:
        if ord(my_letter) >= 97 and ord(my_letter) < 123:
            my_letter = chr(ord(my_letter) - 32)
        print("{:s}".format(my_letter), end='')

    print('\n', end="")
