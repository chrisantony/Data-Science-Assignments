# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sqlite3 as lite
import pandas as pd
import pandas.io.sql as psql
import sys
con = lite.connect('C:\sqlite\weather_history.db')
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS cities")
    cur.execute('CREATE TABLE cities (name text, state text)')
    cur.execute("DROP TABLE IF EXISTS weather")
    cur.execute('''CREATE TABLE weather (city text, year integer, warm_month text,
cold_month text)''')
cur.execute("INSERT INTO cities VALUES('Washington', 'DC')")
cur.execute("INSERT INTO cities VALUES('Houston', 'TX')")
cur.execute("INSERT INTO weather VALUES('Washington', 2013, 'July', 'January')")
cur.execute("INSERT INTO weather VALUES('Houston', 2013, 'July', 'January')")
query_cities = "select * from cities"
cities = pd.read_sql(query_cities,con)
query_weather = "select * from weather"
weather = pd.read_sql(query_weather,con)
weather["name"] = weather["city"]
weather.drop('city', axis=1, inplace=True)
combined = pd.DataFrame.merge(cities,weather, how='inner', left_on = 'name', right_on = 'name')
together = combined.apply(lambda x:'%s, %s' % (x['name'],x['state']),axis=1)
print "cities that are warmest in July are:", ', '.join(together.tolist())
year = 2013
query_weather_dynamic = " SELECT * FROM weather WHERE year = " + str(int(year))
weather_dynamic = psql.read_sql(query_weather_dynamic,con)









    















