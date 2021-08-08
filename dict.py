#!/usr/bin/python

dict = {
    0: "index 0",
    1: "index 1",
    2: "index 2",
}

# append data
dict[3] = 'index 3'

for i in dict:
    print(dict[i])

def dict_search(idx):
    for i in dict:
        if(i == idx):
            return dict[i]
    return "No such index"

print("\nsearch: " + dict_search(0))
print("\nsearch: " + dict_search(100))