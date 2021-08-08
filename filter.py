#!/usr/bin/python

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def filter_odd_number(num):
    return num % 2 == 0

print(list(numbers))
even_numbers = filter(filter_odd_number, numbers)
print(list(even_numbers))