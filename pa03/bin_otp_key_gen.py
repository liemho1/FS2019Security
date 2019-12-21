#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Keygen
"""
Created on Sun Sep  22 11:13:31 2019
@author: lthpkh@umsystem.edu
"""

import os
import sys
import random

#check to see if output file already exists
if os.path.exists(sys.argv[1]):
    os.remove(sys.argv[1])

def main():

    for keyIdent in range(1, 501):
        key=''
        for x in range(0,256):
            # Random bytes
            bytes = os.urandom(64)
            csprng = random.SystemRandom()
            # Random (probably large) integer
            random_int = csprng.randint(0, 255)
            a = str(bin(random_int))
            #remove first 2 characters from a
            b = a[2:]
            #pad string to have 8 bits
            c = str(b).zfill(8)
            #print(c)
            key+=c

        index = str(keyIdent).zfill(3)   
        indexKey = index + " " + key

        with open(sys.argv[1], 'a') as f_out:
            print(indexKey, file=f_out)

if __name__ == '__main__':
    main()


    

 


