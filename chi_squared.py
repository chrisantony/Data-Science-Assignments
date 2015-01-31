# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 09:55:00 2015

@author: Owner
"""


import matplotlib.pyplot as plt
from scipy import stats
import collections
import pandas as pd

# Load the reduced version of the Lending Club Dataset
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
# Drop null rows
loansData.dropna(inplace=True)

freq = collections.Counter(loansData['Open.CREDIT.Lines'])
plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.show()
chi, p = stats.chisquare(freq.values())
print p
print chi