# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 20:57:41 2015

@author: Owner
"""

import pandas as pd
from os.path import join
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from scipy.stats import itemfreq

idealweight = pd.read_csv('C:\Users\Owner\Documents\Thinkful\ideal_weight.csv')

# remove " ' " from column names:
idealweight = pd.read_csv('C:\Users\Owner\Documents\Thinkful\ideal_weight.csv',names = ['id', 'sex', 'actual', 'ideal', 'diff'], header=0)

#remove("'") from column sex:
idealweight["sex"] = idealweight["sex"].map(lambda x: x.replace("'",""))

# to plot the distribution of actual weight and ideal weight:

plt.figure()
x = plt.hist([idealweight['actual'], idealweight['ideal']], histtype = 'bar', stacked=False)
plt.show()

# to plot the distributions of difference in weight
plt.figure()
y = plt.hist([idealweight['diff']], histtype = 'bar', stacked=True)
plt.show()

#Gaussian Distribution:

df = pd.read_csv('C:\Users\Owner\Documents\Thinkful\ideal_weight.csv')

df['gender'] = pd.Categorical(df['sex'].tolist())


gnb = GaussianNB()
data =  idealweight[['actual', 'ideal', 'diff']]
target = idealweight ['gender']
model = gnb.fit(data, target)
y_pred = model.predict(data)

