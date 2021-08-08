#!/usr/bin/python

import getpass as gp

passwd = gp.getpass("Password: ")

if passwd == 'ming':
    print("Welcome back")
else:
    print("Wrong answer")