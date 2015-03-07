# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 16:04:29 2015

@author: Owner
"""

import sqlite3 as lite
import csv
import pandas as pd
import pandas.io.sql as psql
import sys
con = lite.connect ('C:\sqlite\'Baltimore_crime_study.db')
with con:
    cur = con.cursor()

csvfile = open('C:\Users\Owner\Documents\Thinkful.Capstone.Project\CrimeStatistics.csv', 'rb')
creader = csv.reader(csvfile, delimiter=',', quotechar='|')

t = (creader,)

for t in creader:
   
    cur.execute('INSERT INTO CrimeStatistics VALUES (?,?,?,?,?,?,?,?,?,?)', t)

csv.close()
connection.commit()
connection.close()


import sqlite3 as lite
import csv
con = lite.connect ('C:\sqlite\'Baltimore_crime_study.db')
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Speed_Cameras")
    cur.execute('''CREATE TABLE Speed_Cameras(address string, direction string,
    street string, crossStreet string, intersection string, Location string)''')
    
reader = csv.reader(open('C:\Users\Owner\Documents\Thinkful.Capstone.Project\Speed_Cameras.csv','rb'), delimiter=',', quotechar='"')

for row in reader:
    cur.execute('''INSERT INTO Speed_Cameras (address, direction, street, crossStreet, intersection, Location)
    VALUES (?, ?, ?, ?, ?, ?)''')

csvfile.close()
con.commit()
con.close()

