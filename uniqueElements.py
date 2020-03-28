# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 08:59:19 2019

@author: Bisma Naeem
"""

def List_Intersect():
    list1 = []
    list2 =[]
    n=int(input("Enter the total elements of the first list : "))
    print("Enter first list elements:" )
    
    for i in range(0,n):#for input in list2
        num=int(input())
        list1.append(num)
        
    print(list1)       
    
    n2=int(input("Enter the total number of elements in second list:"))
    print("print the elements of second list:")
   
    for i in range(0,n2): #for input in list2
        num2=int(input())
        list2.append(num2)
    print(list2)
    
    ss = set(list1)
    bb = set(list2)
    print("unique element is: ")
    print(ss - bb )
    print(bb-ss)
    
    
   
    #for item in list1: additional code for trial2
	   # for item1 in list2:
             #if (item == item1):
               # print(item)
            # elif(item!=item1):
                #  print("no element found")
         
            
    
       
    
List_Intersect()  