#!/usr/bin/python

# python does not support switch case, so implement ourselves

def switcher(id):
    cases = {
        1: "case 1",
        2: "case 2",
        3: "case 3",
    }
    return cases.get(id, "no such case")

id1 = 1
id2 = 2
id3 = 3

print(switcher(id1))
print(switcher(id2))
print(switcher(id3))
