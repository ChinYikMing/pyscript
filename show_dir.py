#!/usr/bin/python

import os

path = "/home/chinyikming"

files = os.listdir(path)

for file in files:
    print(file)