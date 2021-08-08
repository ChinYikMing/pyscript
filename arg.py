#!/usr/bin/python

import sys

print("argc: %d" % len(sys.argv))

for arg in sys.argv:
    print("arg: %s" % arg)