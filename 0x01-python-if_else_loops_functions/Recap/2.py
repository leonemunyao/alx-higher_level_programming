#!/usr/bin/env python3

"""Check is a character is in a String"""

"""Write a code that asks a user to provide a name of a country that does 
not containn any lowercase a or e letter (Use the prompt: The country is).
If the user provides a correct string (i.e one with no a or e inside it.) print: You won ... unless you made this name up!
Otherwise print: You lost"""

country = input("The country is: ")
if 'a' in country or 'e' in country:
    print("You lost")
elif country == "":
    print("You must provide a name!")
    
else:
    print("You won ... unless you made this name up!")
