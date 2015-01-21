# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 07:45:11 2015

@author: Owner
"""

import matplotlib.pyplot as plt
import pandas as pd
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)
loansData.boxplot(column='Amount.Funded.By.Investors')
plt.show()
loansData.hist(column='Amount.Funded.By.Investors')
plt.show()

import scipy.stats as stats
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="uniform", plot=plt)
plt.show()


import matplotlib.pyplot as plt
import pandas as pd
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)
loansData.boxplot(column='Amount.Requested')
plt.show
loansData.hist(column='Amount.Requested')
plt.show
import scipy.stats as stats
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist='uniform', plot=plt)
plt.show()