#!/usr/bin/python3
for my_letter in range(97, 123):
    if my_letter == 101 or my_letter == 113:
        continue
    print("{}".format(chr(my_letter)), end="")
