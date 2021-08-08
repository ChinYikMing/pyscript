#!/usr/bin/python

fruits = []

fruits.insert(1, "apple")
fruits.insert(1, "banana")
fruits.insert(0, "cake")
fruits.insert(3, "apple")

search = "apple"
apple_cnt = fruits.count("apple")
print("There are %d %s in the list" % (apple_cnt, search))