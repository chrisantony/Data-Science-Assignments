# -*- coding: utf-8 -*-
"""
Created on Tue Feb 03 20:49:29 2015

@author: Owner
"""

import pandas as pd
crimestats = pd.read_csv('C:\Users\Owner\Desktop\CrimeStatistics.csv')
crimestats['CrimeDate'][0:5]
print
x = crimestats['CrimeDate'][0:5].values[1]
print x
x = x.strip('12:00:00 AM')
print x
