#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Get the last digit of the number
last_digit = abs(number) % 10

sign = 1 if number >= 0 else -1
# Print the result
print("Last digit of", number, "is", sign * last_digit, end=" ")

if sign * last_digit > 5:
    print("and is greater than 5")
elif sign * last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
