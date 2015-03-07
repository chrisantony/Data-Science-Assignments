# -*- coding: utf-8 -*-
"""
Created on Tue Mar 03 15:34:18 2015

@author: Owner
"""

import sqlite3 as lite
import pandas as pd
from pandas import DataFrame, Series
from numpy import nan as NA
from geopy.geocoders import Nominatim
import matplotlib.pyplot as plt

con = lite.connect('C:\sqlite\Baltimore_crime_study.db')#connect to the database
with con:
    cur = con.cursor()# create a cursor.
    cur.execute("SELECT * FROM Speed_Camera")
    rows = cur.fetchall()
    cols = [desc[0] for desc in cur.description]
    df = pd.DataFrame(rows, columns = cols)

# cleaning up of the data on Table Speed_Camera:

# column interesection is a combination of street and crossStreet
df['intersection'] = df['street'] + " " + df['crossStreet']
print df['intersection'][0:5] # to verify the above concat opertaion

df.dtypes # to quickly check the column headers and datatypes.

#Location 1 has latitude and longitude co-ordinates.
#Use geopy to draw the actual location from these co-ordinates

geolocator = Nominatim()
x = geolocator.reverse("39.2364856246, -76.6122106478")
#y = geolocator.reverse(coord[1])
location = []
for j in df['Location 1']:
    k = j.replace('(','')
    k = k.replace(')', '')
    add = geolocator.reverse(k)
    location.append(add.address)
    
df['location'] = location
df.dtypes # to check if a new column location has been added.
print df['location'][0:2]

# to find out the 2 most crime prone direction:
df['direction'].unique() # to check the unique records in the column direction
df['direction'].value_counts()[:2]
# The above line shows 2 most crime prone direction: 1) E/B 2) W/B

df.hist(column='direction')
plt.show()

# working on the data from Table CrimeStatistics:

cur.execute("SELECT * FROM CrimeStatistics")
rows = cur.fetchall()
cols = [desc[0] for desc in cur.description]
CS = pd.DataFrame(rows, columns = cols)
CS.dtypes # to check column headers and data types
len(CS) - CS.count()

# to format the data in Crime Time column:
def getSec(s):
    l = s.split(':')
    return int(l[0]) * 3600 + int(l[1]) * 60 + int(l[2])
seconds = []
for i in range(len(CS)):
    if ((':' in str(CS['CrimeTime'][i])) == True):
        s = getSec(str(CS['CrimeTime'][i]))
    else:
        s = CS['CrimeTime'][i]
    seconds.append(s)
CS['CrimeTimeinSeconds'] = seconds
CS.dtypes
print CS['CrimeTimeinSeconds'][0:10]


CS['CrimeCode'].value_counts()[:5]
# to find the top 5 CrimeCodes

#histogram of weapons
CS.hist(column='Weapon')
plt.show()

#to check different weapons used in the crime:
CS['Weapon'].unique()
CS['District'].unique()

a = pd.read_sql("SELECT COUNT (*)FROM CrimeStatistics GROUP BY Weapon",con)
print a

b = pd.read_sql("SELECT COUNT (*) FROM CrimeStatistics GROUP BY District",con)
print b

c = pd.read_sql("SELECT COUNT(*) FROM CrimeStatistics GROUP BY District, Neighborhood",con)
print c

# working on the table Parking _Citations:

query_ParkingCitations="select * from Parking_Citations"
PC = pd.read_sql(query_ParkingCitations,con)
PC.dtypes # to check column headers and datatypes
len(PC) - PC.count()
PC['violCode'].unique()
PC['make'].unique()

D = pd.read_sql("SELECT COUNT (*) FROM Parking_Citations GROUP BY violCode",con)
print D

