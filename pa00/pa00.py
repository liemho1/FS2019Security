#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The first line is a shebang.
# The python3 part could be bash, zsh, ruby, whatever
# There are many ways to do a shebang, this is the best!

"""
Created on Tue Jan 22 23:21:14 2019

@author: youremail@mst.edu
"""
import sys

f_in = open(sys.argv[1], 'r')
line = f_in.readline()
f_in.close()

num = ''
repeat = ''

for letter in line:
    if letter == '\n':
        break
    elif letter.isdigit():
        num = num + letter
    else:
        repeat = repeat + letter

with open(sys.argv[2], 'w') as f_out:
    print(repeat, file=f_out)

for x in range(1,int(num)):
    with open(sys.argv[2], 'a') as f_out:
        print(repeat, file=f_out)