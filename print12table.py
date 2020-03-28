# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 21:25:15 2019

@author: Bisma Naeem
"""

file = open("C:\\Users\\Bisma Naeem\\Desktop\\names.txt","r")
dict_names ={}

for line in file:
    x= line.split(",")
    a = x[0]
    b=x[4]
    dict_names[a]=b
    