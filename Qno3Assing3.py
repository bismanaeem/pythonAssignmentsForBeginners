# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 04:03:49 2019

@author: Bisma Naeem
"""

#Qno3 Print the number of characters of the list
f = open('C:\\Users\\Bisma Naeem\Desktop\Alice1.txt',"r")
My_words =list(map(lambda w:w.split(),f.read()))
print (My_words)
f.close()