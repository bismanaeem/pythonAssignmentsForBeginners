# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 03:25:05 2019

@author: Bisma Naeem
"""

#Read the text file of the chapter one Alice in the wonderland

f = open('C:\\Users\\Bisma Naeem\Desktop\Alice1.txt',"r")
My_words =list(map(lambda w:w.split(),f.readlines()))
print (My_words)

##without lambda function

#words = f.read().split()
#print(words)

#Qno2 answer
#print the total length of the string
print(len(My_words))

f.close()