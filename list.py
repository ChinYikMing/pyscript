#!/usr/bin/python

fruits = []

fruits.insert(1, "apple")
fruits.insert(1, "banana")
fruits.insert(0, "cake")

print("Initial")
for f in fruits:
    print(f)

print("\ndelete banana")
fruits.remove("banana")
for f in fruits:
    print(f)