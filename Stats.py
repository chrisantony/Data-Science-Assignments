# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 19:07:23 2015

@author: Owner
"""

import pandas as pd
from scipy import stats
data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''
#This is to split the string on new lines
data = data.splitlines()

#then spplit each item in the list on the commas
data = [i.split(',') for i in data]

#Create a pandas dataframe
column_names = data[0] #This is the header
data_rows = data[1::] #These are the rows of data under the header
df = pd.DataFrame(data_rows, columns=column_names)

#The data is now contained in a pandas dataframe.
#Now to proceede with the various calculations

#1st step: To convert the columns to float
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

#Mean Calculation:

alc = df['Alcohol'].mean()
"print mean is %.2f" %(alc)
tob = df['Tobacco'].mean()
print "The mean of the alcohol and tobacco is %.2f %.2f" %(alc, tob)









