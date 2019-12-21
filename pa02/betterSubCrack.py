#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 06:13:31 2019
@author: lthpkh@umsystem.edu
"""

import sys
import os
import random
import collections
import operator
from collections import OrderedDict

import re, copy, pyperclip, simpleSubCipher, wordPatterns, makeWordPatterns
nonLettersOrSpacePattern = re.compile('[^A-Z\s]')

#check to see if output file already exists
if os.path.exists(sys.argv[2]):
    os.remove(sys.argv[2])





LETTERS = ' .ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lettersList = set(LETTERS)


def main():
    mostFreqToLeast = ' ETOARNIHSLDCUBGWFYPMK.XJQVZ'
    first = ' ETOARNIHSLDCUBGWFYPMK.XJQVZ'

    with open(sys.argv[1], 'r') as f_in:
        message0 = f_in.read()
        #print(contents)


    
    letter_freq = {} 
    for i in message0.upper(): 
        if i in letter_freq: 
            letter_freq[i] += 1
        else: 
            letter_freq[i] = 1


    #for key,val in letter_freq.items():
    #    print(key, "=>", val)

    #print("--------------------")
    
    matched_letters = {}
    #remove all keys that do not match letter set
    for (key,val) in letter_freq.items():
        if key in lettersList:
            #print(key)
            matched_letters[key] =val 

    #for (key,val) in matched_letters.items():
    #    print(key, "=>", val)
    
    #print("--------------------")
    
    sortByVals = OrderedDict(sorted(matched_letters.items(), key=lambda x: x[1], reverse = True))
    
    #a = sorted(matched_letters.keys())
    #print(a)

    #print()

    #for k, v in sortByVals.items():
    #    print (k, ":" , v)

    #print(sortByVals)


    #sortByVals['G'] = 'F'

    #print(sortByVals)

    charsB = ''
    #create list of letters from most freq to least
    for k in sortByVals.keys():
        #print(k)
        charsB += k

    

#
    #print("after swap:",new)
#
    #for i in range(0, len(mostFreqToLeast)):
    #    if(mostFreqToLeast[i] == 'B'):
    #        index1 = i
    #    elif(mostFreqToLeast[i] == ebook[1].upper()):
    #        index2 = i
#
    #print(mostFreqToLeast)
    #new1 = swap(mostFreqToLeast, index1,index2)
    #print(new1)
    #for i in range(0, len(new1)):
    #    if(new1[i] == 'O'):
    #        index1 = i
    #    elif(new1[i] == ebook[2].upper()):
    #        index2 = i
#
    #new2 = swap(new1, index1,index2)
    #for i in range(0, len(new2)):
    #    if(new2[i] == 'K'):
    #        index1 = i
    #    elif(new2[i] == ebook[4].upper()):
    #        index2 = i
#
    #new3 = swap(new2, index1,index2)
    #for i in range(0, len(new3)):
    #    if(new3[i] == ' '):
    #        index1 = i
    #    elif(new3[i] == ebook[5].upper()):
    #        index2 = i
#
    #new4 = swap(new3, index1,index2)





    


    a = list(sortByVals.keys())
    #charsB = a

    message = ''
    charsA = mostFreqToLeast
    #charsB = list(sortByVals)
    charsA, charsB = charsB, charsA

    # Loop through each symbol in message:
    for symbol in message0:
        if symbol.upper() in charsA:
            # Encrypt/decrypt the symbol:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                message += charsB[symIndex].upper()
            else:
                message += charsB[symIndex].lower()
        else:
            # Symbol is not in LETTERS; just add it
            message += symbol
    

    #
    ##print(translated)
    #with open(translated, "a") as f_out:
    #    f_out.write(translated)
    #translated = message
    ebook = ''
    for i in range(0, len(message)):
        if(message[i] == '#'):
            ebook += message[i-6]
            ebook += message[i-5]
            ebook += message[i-4]
            ebook += message[i-3]
            ebook += message[i-2]
            ebook += message[i-1]
            hashy = i
            break

            
    web = ''
    for i in range(0, len(message)):
        if((message[i] == '/') and (message[i+1] == '/') 
            and message[i-1] == ':'):
            web += message[i+2]
            web += message[i-2]
            web += message[i-3]
            web += message[i-4]
            web += message[i+5]
            break
 
    star = ''
    for i in range(0, len(message)):
        if(message[i] == '*' and message[i+1] == '*'
            and message[i+2] == '*'):
            star += message[i+4] #S
            star += message[i+5] #T
            star += message[i+6] #A star[2]
            star += message[i+7] #R
            star += message[i+8] #T
            
            star += message[i+15] #I
            star += message[i+14] #H
            star += message[i+11] #F
            star += message[i+21] #j
            star += message[i+23] #c
            star += message[i+26] #g
            break


    for i in range(0, len(mostFreqToLeast)):
        if(mostFreqToLeast[i].upper() == 'S'):
            ii=i
        if(mostFreqToLeast[i].upper() == star[0].upper()):
            jj=i
    mostFreqToLeast = swap(mostFreqToLeast,ii,jj)






    for i in range(0, len(mostFreqToLeast)):
        if(mostFreqToLeast[i].upper() == 'T'):
            ii=i
        if(mostFreqToLeast[i].upper() == star[1].upper()):
            jj=i
    mostFreqToLeast = swap(mostFreqToLeast,ii,jj)

    for i in range(0, len(mostFreqToLeast)):
        if(mostFreqToLeast[i].upper() == 'A'):
            ii=i
        if(mostFreqToLeast[i].upper() == star[2].upper()):
            jj=i
    mostFreqToLeast = swap(mostFreqToLeast,ii,jj)
    for i in range(0, len(mostFreqToLeast)):
        if(mostFreqToLeast[i].upper() == 'R'):
            ii=i
        if(mostFreqToLeast[i].upper() == star[3].upper()):
            jj=i
    mostFreqToLeast = swap(mostFreqToLeast,ii,jj)


    



    for i in range(0, len(mostFreqToLeast)):
        if(mostFreqToLeast[i].upper() == 'B'):
            ii=i
        if(mostFreqToLeast[i].upper() == ebook[1].upper()):
            jj=i
    mostFreqToLeast = swap(mostFreqToLeast,ii,jj)




    #for i in range(0, len(mostFreqToLeast)):
    #    if(mostFreqToLeast[i].upper() == 'O'):
    #        ii=i
    #    if(mostFreqToLeast[i].upper() == ebook[2].upper()):
    #        jj=i
    #mostFreqToLeast = swap(mostFreqToLeast,ii,jj)

    #for i in range(0, len(mostFreqToLeast)):
    #    if(mostFreqToLeast[i].upper() == 'F'):
    #        ii=i
    #    if(mostFreqToLeast[i].upper() == star[7].upper()):
    #        jj=i
    #mostFreqToLeast = swap(mostFreqToLeast,ii,jj)
    for i in range(0, len(mostFreqToLeast)):
        if(mostFreqToLeast[i].upper() == 'K'):
            ii=i
        if(mostFreqToLeast[i].upper() == ebook[4].upper()):
            jj=i
    mostFreqToLeast = swap(mostFreqToLeast,ii,jj)



    print(first)
    print(mostFreqToLeast)
        



    #print(mostFreqToLeast)    
    #print(mostFreqToLeast)

    print(star[2])

    #
    #newtrans = ''
    #for i in translated:
    #    if(i.upper() == ebook[1].upper()):
    #        if i.isupper():
    #            newtrans += 'B'
    #        else:
    #            newtrans += 'b'
    #    elif(i.upper() == ebook[0].upper()):
    #        if i.isupper():
    #            newtrans += 'E'
    #        else:
    #            newtrans += 'e'
    #    elif(i.upper() == ebook[2].upper()):
    #        if i.isupper():
    #            newtrans += 'O'
    #        else:
    #            newtrans += 'o'
    #    elif(i.upper() == ebook[4].upper()):
    #        if i.isupper():
    #            newtrans += 'K'
    #        else:
    #            newtrans += 'k'
    #    elif(i.upper() == web[0].upper()):
    #        if i.isupper():
    #            newtrans += 'W'
    #        else:
    #            newtrans += 'w'
    #    elif(i.upper() == web[1].upper()):
    #        if i.isupper():
    #            newtrans += 'P'
    #        else:
    #            newtrans += 'p'
    #    elif(i.upper() == web[2].upper()):
    #        if i.isupper():
    #            newtrans += 'T'
    #        else:
    #            newtrans += 't'
    #    #elif(i.upper() == web[3].upper()):
    #    #    if i.isupper():
    #    #        newtrans += 'H'
    #    #    else:
    #    #        newtrans += 'h'
    #    elif(i.upper() == web[4].upper()):
    #        if i.isupper():
    #            newtrans += '.'
    #        else:
    #            newtrans += '.'
    #    elif(i.upper() == star[0].upper()):
    #        if i.isupper():
    #            newtrans += 'S'
    #        else:
    #            newtrans += 's'
    #    elif(i.upper() == star[2].upper()):
    #        if i.isupper():
    #            newtrans += 'A'
    #        else:
    #            newtrans += 'a'
    #    elif(i.upper() == star[3].upper()):
    #        if i.isupper():
    #            newtrans += 'R'
    #        else:
    #            newtrans += 'r'
    #    elif(i.upper() == star[5].upper()):
    #        if i.isupper():
    #            newtrans += 'I'
    #        else:
    #            newtrans += 'i'
    #    elif(i.upper() == star[6].upper()):
    #        if i.isupper():
    #            newtrans += 'H'
    #        else:
    #            newtrans += 'h'
    #    elif(i.upper() == star[7].upper()):
    #        if i.isupper():
    #            newtrans += 'F'
    #        else:
    #            newtrans += 'f'
    #    elif(i.upper() == star[8].upper()):
    #        if i.isupper():
    #            newtrans += 'J'
    #        else:
    #            newtrans += 'j'
    #    elif(i.upper() == star[9].upper()):
    #        if i.isupper():
    #            newtrans += 'C'
    #        else:
    #            newtrans += 'c'
    #    elif(i.upper() == star[10].upper()):
    #        if i.isupper():
    #            newtrans += 'G'
    #        else:
    #            newtrans += 'g'
    #    elif(i.upper() == charsB[0].upper()):
    #        if i.isupper():
    #            newtrans += ' '
    #        else:
    #            newtrans += ' '
    #    
    #    else:
    #        newtrans += i
#



    translated = ''
    charsA = mostFreqToLeast
    #charsB = list(sortByVals)
    charsA, charsB = charsB, charsA

    # Loop through each symbol in message:
    for symbol in message:
        if symbol.upper() in charsA:
            # Encrypt/decrypt the symbol:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # Symbol is not in LETTERS; just add it
            translated += symbol

#    for x in range(0, len(newtrans)):
#        if(newtrans[hashy-x] == ':' and (newtrans[hashy-x-13]=='\\n')):
#            print(newtrans[hashy-x-1])
#            print(newtrans[hashy-x-2])
#            print(newtrans[hashy-x-3])
#            print(newtrans[hashy-x-4])
#            print(newtrans[hashy-x-5])
#            
#            print(newtrans[hashy-x-6])
#            print(newtrans[hashy-x-7])
#            print(newtrans[hashy-x-8])
#            print(newtrans[hashy-x-9])
#            print(newtrans[hashy-x-10])
#
#            print(newtrans[hashy-x-11])
#            print(newtrans[hashy-x-12])
#            print(newtrans[hashy-x-13])
#            break
        #print("hello")
    ##print(a)
#
#
#
#
    #for i in range(0, len(message)):
    #    if(message[i] == '#'):
    #        print(message[i-1],message[i-2],message[i-3],message[i-4],message[i-5],message[i-6])
#

 # Determine the possible valid ciphertext translations:
   # print('Hacking...')
    #letterMapping = hackSimpleSub(newtrans)
#
   # # Display the results to the user:
   # print('Mapping:')
   # print(letterMapping)
   # print()
#
   # print('Original ciphertext:')
   # print(translated)
   # print()
   # print('Copying hacked message to clipboard:')
    #hackedMessage = decryptWithCipherletterMapping(newtrans, letterMapping)
   # pyperclip.copy(hackedMessage)
   # print(hackedMessage)




    with open(sys.argv[2], 'a') as f_out:
        print(translated, file=f_out)








    #print("before swap:", mostFreqToLeast)         
    #  
    ##print(ebook.upper())
#
    #index1 = 0
    #index2 = 0
#
    #for i in range(0, len(mostFreqToLeast)):
     #   if(mostFreqToLeast[i] == 'E'):
    #        index1 = i
    #    elif(mostFreqToLeast[i] == ebook[0].upper()):
    #        index2 = i
    
    #new = swap(mostFreqToLeast, index1,index2)

    



#
    #translated = ''
    #charsA = mostFreqToLeast
    ##charsB = list(sortByVals)
    #charsA, charsB = charsB, charsA
#
    ## Loop through each symbol in message:
    ##for symbol in message:
    ##    if symbol.upper() in charsA:
    ##        # Encrypt/decrypt the symbol:
    ##        symIndex = charsA.find(symbol.upper())
    #        if symbol.isupper():
    #            translated += charsB[symIndex].upper()
    #        else:
    #            translated += charsB[symIndex].lower()
    #    else:
    #        # Symbol is not in LETTERS; just add it
    #        translated += symbol

    #with open(sys.argv[2], 'a') as f_out:
    #    print(translated, file=f_out)


def swap(s, i, j):
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)

def getBlankCipherletterMapping():
    # Returns a dictionary value that is a blank cipherletter mapping.
    return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': [], ' ': [], '.': []}


def addLettersToMapping(letterMapping, cipherword, candidate):
    # The `letterMapping` parameter is a "cipherletter mapping" dictionary
    # value that the return value of this function starts as a copy of.
    # The `cipherword` parameter is a string value of the ciphertext word.
    # The `candidate` parameter is a possible English word that the
    # cipherword could decrypt to.

    # This function adds the letters of the candidate as potential
    # decryption letters for the cipherletters in the cipherletter
    # mapping.


    for i in range(len(cipherword)):
        if candidate[i] not in letterMapping[cipherword[i]]:
            letterMapping[cipherword[i]].append(candidate[i])



def intersectMappings(mapA, mapB):
    # To intersect two maps, create a blank map, and then add only the
    # potential decryption letters if they exist in BOTH maps.
    intersectedMapping = getBlankCipherletterMapping()
    for letter in LETTERS:

        # An empty list means "any letter is possible". In this case just
        # copy the other map entirely.
        if mapA[letter] == []:
            intersectedMapping[letter] = copy.deepcopy(mapB[letter])
        elif mapB[letter] == []:
            intersectedMapping[letter] = copy.deepcopy(mapA[letter])
        else:
            # If a letter in mapA[letter] exists in mapB[letter], add
            # that letter to intersectedMapping[letter].
            for mappedLetter in mapA[letter]:
                if mappedLetter in mapB[letter]:
                    intersectedMapping[letter].append(mappedLetter)

    return intersectedMapping


def removeSolvedLettersFromMapping(letterMapping):
    # Cipherletters in the mapping that map to only one letter are
    # "solved" and can be removed from the other letters.
    # For example, if 'A' maps to potential letters ['M', 'N'], and 'B'
    # maps to ['N'], then we know that 'B' must map to 'N', so we can
    # remove 'N' from the list of what 'A' could map to. So 'A' then maps
    # to ['M']. Note that now that 'A' maps to only one letter, we can
    # remove 'M' from the list of letters for every other
    # letter. (This is why there is a loop that keeps reducing the map.)

    loopAgain = True
    while loopAgain:
        # First assume that we will not loop again:
        loopAgain = False

        # `solvedLetters` will be a list of uppercase letters that have one
        # and only one possible mapping in `letterMapping`:
        solvedLetters = []
        for cipherletter in LETTERS:
            if len(letterMapping[cipherletter]) == 1:
                solvedLetters.append(letterMapping[cipherletter][0])

        # If a letter is solved, than it cannot possibly be a potential
        # decryption letter for a different ciphertext letter, so we
        # should remove it from those other lists:
        for cipherletter in LETTERS:
            for s in solvedLetters:
                if len(letterMapping[cipherletter]) != 1 and s in letterMapping[cipherletter]:
                    letterMapping[cipherletter].remove(s)
                    if len(letterMapping[cipherletter]) == 1:
                        # A new letter is now solved, so loop again.
                        loopAgain = True
    return letterMapping


def hackSimpleSub(message):
    intersectedMap = getBlankCipherletterMapping()
    cipherwordList = nonLettersOrSpacePattern.sub('', message.upper()).split()
    for cipherword in cipherwordList:
        # Get a new cipherletter mapping for each ciphertext word:
        candidateMap = getBlankCipherletterMapping()

        wordPattern = makeWordPatterns.getWordPattern(cipherword)
        if wordPattern not in wordPatterns.allPatterns:
            continue # This word was not in our dictionary, so continue.

        # Add the letters of each candidate to the mapping:
        for candidate in wordPatterns.allPatterns[wordPattern]:
            addLettersToMapping(candidateMap, cipherword, candidate)

        # Intersect the new mapping with the existing intersected mapping:
        intersectedMap = intersectMappings(intersectedMap, candidateMap)

    # Remove any solved letters from the other lists:
    return removeSolvedLettersFromMapping(intersectedMap)


def decryptWithCipherletterMapping(ciphertext, letterMapping):
    # Return a string of the ciphertext decrypted with the letter mapping,
    # with any ambiguous decrypted letters replaced with an _ underscore.

    # First create a simple sub key from the letterMapping mapping:
    key = ['x'] * len(LETTERS)
    for cipherletter in LETTERS:
        if len(letterMapping[cipherletter]) == 1:
            # If there's only one letter, add it to the key.
            keyIndex = LETTERS.find(letterMapping[cipherletter][0])
            key[keyIndex] = cipherletter
        else:
            ciphertext = ciphertext.replace(cipherletter.lower(), '_')
            ciphertext = ciphertext.replace(cipherletter.upper(), '_')
    key = ''.join(key)

    # With the key we've created, decrypt the ciphertext:
    return simpleSubCipher.decryptMessage(key, ciphertext)



if __name__ == '__main__':
    main()