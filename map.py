#!/usr/bin/python

numbers = [2, 3, 4]

x = 2

def cal(n):
    return x ** n

print(list(numbers))
cal_result = map(cal, numbers)
print(list(cal_result))