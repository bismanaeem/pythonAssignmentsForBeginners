# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 22:56:43 2019

@author: Bisma Naeem
"""

#Pangram 

str1 = input("please enter a string to check whether its a pangram or not: ")

def pangram_Check(str1):
    alphabets ="abcdefghijklmnopqrstuvwxyz"
    for char in alphabets:
        if(char not in str1.lower()):
            return False
        else:
            return True
        
if(pangram_Check(str1) == True):
    print("The string is pangram")
else:
    print("The string is not a pangram ")