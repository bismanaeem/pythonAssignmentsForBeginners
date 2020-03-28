# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 04:07:18 2019

@author: Bisma Naeem
"""

#Qno4 Print the words of the list in uppercase
f = open('C:\\Users\\Bisma Naeem\Desktop\Alice1.txt',"r")
My_words =list(map(lambda w:w.upper().split(),f.readlines()))
print (My_words)
f.close()