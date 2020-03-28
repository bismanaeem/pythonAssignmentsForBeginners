# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 08:42:57 2019

@author: Bisma Naeem
"""

#Lowercase and uppercase function

def LowerCase_Upper_Func():
    stringnew=input("Enter a string:")
    l=0
    u=0
    for i in stringnew:
      if(i.islower()):
            l=l+1
      elif(i.isupper()):
            u=u+1
            
            
    print("Lower case letters of string: ")    
    print(l)
    print("Upper case letters of string: ")
    print(u)
    
LowerCase_Upper_Func()
