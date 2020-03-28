# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 10:14:08 2019

@author: Bisma Naeem
"""

#Qno9 Python Program that accepts the hyphen separated input and generates output with hyphen


def Hyphen_Separated_Function():
    print("enter a list of hyphen separated sequence: ")
    listi=[n for n in input().split('-')]
    listi.sort()
    print("sorted:")
    print('-'.join(listi))
 
    
Hyphen_Separated_Function()    