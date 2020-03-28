# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 07:22:46 2019

@author: Bisma Naeem
"""

#Qno6 words whose length is equal and greater than 3
f = open('C:\\Users\\Bisma Naeem\Desktop\Alice1.txt',"r")
My_words =list(map(lambda w:w.split(),f.readlines()))

txt = list(filter(lambda z:[len(My_words)>=3],My_words))
print(txt)
#logical error