# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sqlite3 as lite
import pandas as pd
con = lite.connect('C:\sqlite\getting_started.db')
cur = con.cursor()
query_weather = "select * from weather"
weather = pd.read_sql(query_weather,con)
print weather
query_cities = "select * from cities"
cities = pd.read_sql(query_cities,con)
print cities
