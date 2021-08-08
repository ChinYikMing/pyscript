#!/usr/bin/python

x = 4
n = 3

power = x ** n  # power now should be 64
print("%d to the power %d is %d" % (x, n, power))

power = pow(x,n)
print("%d to the power %d is %d" % (x, n, power))

import math 
power = math.pow(x,n)
print("%d to the power %d is %d" % (x, n, power))