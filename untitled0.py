# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 05:55:43 2019

@author: Bisma Naeem
"""
import sqlite3



conn = sqlite3.connect('customer_master_db')

curs = conn.cursor()

sqlcmd = 'CREATE TABLE customer_master(cust_id integer primary key, cust_fname char(20), cust_lname char(20),cust_address char(30), cust_pincode integer(8), mobileno integer(10),email_id char(50),cust_password char(10))'

curs.execute(sqlcmd)

print("CUSTOMER MASTER TABLE CREATED\n")