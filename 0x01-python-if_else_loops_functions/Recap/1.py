#!/usr/bin/env python3

"""Write a Python program that will ask the user the following question

Is Sydney the capital of Australia?

If the user answer is y, print: Wrong! Canberra is the capital!
if the user answer is n, print: Correct!
If the user answer is anything else, print: I do not understand your answer!"""

answer = input('Is Sydney the capital of Australia? ')
if answer == 'y':
    print("Wrong! Canberra is the capital!")
elif answer == "n":
    print("Correct!")
else:
    print("I do not understand your answer!")
