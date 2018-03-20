#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 14:57:40 2017

@author: ireneyaejinnam
"""



def piggify(word):
    vowels = 'aeiou'
    x = -1
    if word[0] in vowels:
        return word+"yay"
    else:
        for char in word:
            x += 1
            if char in vowels:
                return word[x:]+word[0:x]+'ay'
            
while True:
    word = input("Enter a word to piggify.")
    if word == '.':
        break
    else:
        print (piggify(word))