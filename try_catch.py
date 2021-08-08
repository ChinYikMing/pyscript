#!/usr/bin/python

try:
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

except (NameError):
    print("Please enter a numeric value")