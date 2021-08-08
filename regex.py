#!/usr/bin/python

import re

string = "APPLE"
pattern = "^[A-Z]"

found = re.match(pattern, string)

if found:
    print("Found")
else:
    print("Not found")
