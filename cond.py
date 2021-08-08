#!/usr/bin/python

cond1 = True
cond2 = True

if(cond1 and cond2):
    print("cond1 and cond2 are True")
elif(not cond1 and cond2):
    print("cond1 is False and cond2 is True")
elif(cond1 and not cond2):
    print("cond1 is True and cond2 is False")
else:
    print("cond1 nd cond2 are False")

cond1 = False
cond2 = True

if(cond1 and cond2):
    print("cond1 and cond2 are True")
elif(not cond1 and cond2):
    print("cond1 is False and cond2 is True")
elif(cond1 and not cond2):
    print("cond1 is True and cond2 is False")
else:
    print("cond1 nd cond2 are False")

cond1 = True
cond2 = False

if(cond1 and cond2):
    print("cond1 and cond2 are True")
elif(not cond1 and cond2):
    print("cond1 is False and cond2 is True")
elif(cond1 and not cond2):
    print("cond1 is True and cond2 is False")
else:
    print("cond1 nd cond2 are False")

cond1 = False
cond2 = False

if(cond1 and cond2):
    print("cond1 and cond2 are True")
elif(not cond1 and cond2):
    print("cond1 is False and cond2 is True")
elif(cond1 and not cond2):
    print("cond1 is True and cond2 is False")
else:
    print("cond1 nd cond2 are False")