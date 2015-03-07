# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import sqlite3 as lite
con = lite.connect('C:\sqlite\getting_started.db')
with con:
    cur = con.cursor()
    cur.execute('''SELECT name, state, year, warm_month, cold_month 
FROM cities 
    INNER JOIN weather 
    ON name = city''')
rows = cur.fetchall()
print rows


 






