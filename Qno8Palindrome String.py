# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 10:04:48 2019

@author: Bisma Naeem
"""

#Qno 8
#Check whether the string entered by the user is a palindrome or not
str1 = input("please enter a string to check whether its a PALINDROME or not:")

def Palindrome_Str(str1):
    str2 = str1[::-1]
    print(str2)
    if(str2==str1):
        print("The entered string is a palindrome")
    else:
        print("the string you entered is not a palindrome")    
Palindrome_Str(str1)       