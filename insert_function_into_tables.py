# -*- coding: utf-8 -*-
"""
Created on Tue Dec 30 22:18:25 2014

@author: Owner
"""

import sqlite3 as lite
con = lite.connect ('C:\sqlite\getting_started.db')
cur = con.cursor()
cur.execute('SELECT SQLITE_VERSION()')
data = cur.fetchone ()
print "SQLite version: %s" % data

import sqlite3 as lite
con = lite.connect('C:\sqlite\getting_started - Copy.db')
cur = con.cursor()
cur.execute("INSERT INTO cities VALUES('Washington', 'DC')")
cur.execute("INSERT INTO cities VALUES('Houston', 'TX')")
cur.execute("INSERT INTO weather VALUES('Washington', 2013, 'July', 'January', 95)")
cur.execute("INSERT INTO weather VALUES('Houston', 2013, 'July', 'January', 99)")
con.commit()
print "Records created successfully"
con.close()

import sqlite3 as lite
con = lite.connect('C:\sqlite\getting_started.db')
with con:
   cur = con.cursor()
   cur.execute('''SELECT name, state, year, warm_month, cold_month 
FROM cities 
INNER JOIN weather 
    ON name = city;''')

    
    


 

 















