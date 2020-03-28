# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 10:36:05 2019

@author: Bisma Naeem
"""

#Qno10
#checking whether the string is pangram or not

from string import ascii_lowercase as lowerc
def check_num(s):
    return set(lowerc)-set(s.lower())==set([])
stri = input("enter a sring: ")
if(check_num(stri)==True):
    print("The string is pangram")
else:
    print("The string is not pangram")

 
    
    