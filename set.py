#!/usr/bin/python

# set will only contains unique data
numbers = {23, 90, 100, 23, 43}

# only print 23 once
for num in numbers:
    print(num)

print("Adding 101")
numbers.add(101)
for num in numbers:
    print(num)

