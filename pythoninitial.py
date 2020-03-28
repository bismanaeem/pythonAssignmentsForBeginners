# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 22:19:24 2019

@author: Bisma Naeem
"""

def sameProcessDifferentMethod(username,password):
        AUTH_USERNAME = username
        AUTH_PASSWORD = "SECRET"
        
        if username==AUTH_USERNAME and password ==AUTH_PASSWORD:
            return "welcome"
        
        return "Invalid"
    
username = str(input("Enter username:"))
password=str(input("Enter password:"))

print(sameProcessDifferentMethod(username,password))

    