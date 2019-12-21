#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Encrypt and Decrypt
"""
Created on Sun Sep  22 11:13:31 2019
@author: lthpkh@umsystem.edu
"""

import os
import sys

#grab key from 

def main():
    #grab specific key
    with open(sys.argv[1], "r") as f_in:
        key = f_in.readlines()[int(sys.argv[2])-1]
    key = key[4:]

    #grab input file
    with open(sys.argv[3], "rb") as f_in:
        inputString = f_in.read()

    inputString = inputString.decode('UTF-8')
    #change ASCII to binary
    inputBinary = stringToBinary(inputString)

    #XOR key with message
    inputXORkey = ''
    for i in range(0,256):
        
        #grab first 8 bits from inputLine and key
        wordInput = ''
        wordKey = ''
        for x in range(0,8):
            wordInput += inputBinary[x]
            #print(wordIn)
            wordKey += key[x]
    
        inputXORkey += XOR(wordInput, wordKey)

        #remove first 8 characters from input and key
        inputBinary = inputBinary[8:]
        key = key[8:]


    #transform binary XOR output to string
    outputMessage = ''
    for i in range(0,256):
        
        #grab first 8 bits from inputLine and key
        outputWord = ''
        for x in range(0,8):
            outputWord += inputXORkey[x]
    
        outputMessage += binaryToChar(outputWord)

        #remove first 8 characters from encrypted message
        inputXORkey = inputXORkey[8:]
 
    #print(outputMessage)

    with open(sys.argv[4], 'w') as f_out:
        print(outputMessage, file=f_out)


#xor binary forms
def XOR(word, key):
    xor = ''
    for i in range(0,8):
        if(word[i] == key[i]):
            xor += '0'
        else:
            xor +='1'
    return xor

#transform char to binary
def charToBinary(c):
    binaryForm = str(bin(ord(c)))
    binaryForm = binaryForm[2:]
    return str(binaryForm).zfill(8)

#transform binary to ASCII char
def binaryToChar(c):
    intVal = int(c,2)
    return chr(intVal)

#stringTobinary
def stringToBinary(line):
    stringToBinary = ''
    for c in range(0, 256):
        #print(c)
        #print(line[c])
        binaryChar = str(bin(ord(line[c])))
        binaryChar = binaryChar[2:]
        stringToBinary += str(binaryChar).zfill(8)
    return stringToBinary


if __name__ == '__main__':
    main()
