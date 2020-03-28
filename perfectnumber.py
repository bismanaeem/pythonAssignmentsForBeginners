# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 09:52:15 2019

@author: Bisma Naeem
"""
n=int(input("Enter the number to be checked for a perfect number or not:"))
def perfect_Check(n):
    sum_num = 0
    for a in range(1, n):
        if n % a == 0:
            sum_num += a
    return sum_num == n
print("the enter number is a perfect number:")
print(perfect_Check(n))