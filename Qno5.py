# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 04:21:08 2019

@author: Bisma Naeem
"""

#Qno5
#To print the letters of the list that starts with A or a
f = open('C:\\Users\\Bisma Naeem\Desktop\Alice1.txt',"r")
My_words =list(map(lambda w:w.split(),f.read()))
file = list(filter(lambda item:My_words.start('a'),f.read()))
print(file)

f.close()

#print ( list(filter(lambda x:x.lower().startswith("A"),My_words)))
#logical error