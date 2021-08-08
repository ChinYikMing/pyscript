#!/usr/bin/python

filename = "text.txt"

fd = open(filename, "w")

fd.write("Hello")
fd.write("World")

fd.close()

fd = open(filename, "r")

for line in fd:
    print(line)

fd.close()