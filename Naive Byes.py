# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 22:11:48 2015

@author: Owner
"""

import pandas as pd
idealweight = pd.read_csv('C:\Users\Owner\Documents\Thinkful\ideal_weight.csv')

# the below is to remove"'" from teh headers:
idealweight = pd.read_csv('C:\Users\Owner\Documents\Thinkful\ideal_weight.csv',names = ['id', 'sex', 'actual', 'ideal', 'diff'], header=0)

# the below line is to verify the changes made on column header fields.
y = idealweight.columns.values.tolist() # to list the column headers in the dataframe
print y

#remove("'") from column sex:
idealweight["sex"] = idealweight["sex"].map(lambda x: x.replace("'",""))
z = idealweight["sex"][0:5]
print z


from os.path import join
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB

# PLOT DISTRIBUTION OF ACTUAL WEIGHT VERSUS IDEAL WEIGHT

plt.figure()
y = plt.hist([idealweight['actual'], idealweight['ideal']], histtype='bar', stacked=False)
y = plt.hist([idealweight['diff']], histtype='bar', stacked=False)
plt.show()

#Gaussian Distribution:


idealweight['gender'] = pd.Categorical(idealweight['sex'].tolist())


gnb = GaussianNB()
data = idealweight[['actual','ideal','diff']]
target = idealweight['gender']
model = gnb.fit(data, target)
y_pred = model.predict(data)
print("Number of mislabeled points out of a total %d points: %d" %(data.shape[0], (target != y_pred).sum()))


d = {'actual' : 145,'ideal' : 160, 'diff': -15}
df = pd.DataFrame(data=d, index=[1])
pred = model.predict(df)
print pred

y_pred

from scipy.stats import itemfreq
itemfreq(y_pred)