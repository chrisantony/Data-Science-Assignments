# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 09:19:37 2015

@author: Owner
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm



loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#cleaning up the columns

# to remove % symbol from Interest.Rate column
loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: x.rstrip('%'))

#to remove the word 'months' from loan.length
loansData['Loan.Length'] = loansData['Loan.Length'].map(lambda x: x.rstrip('months'))

# print to veriffy the changes:
print loansData['Interest.Rate'][0:5]
print loansData['Loan.Length'][0:5]
loansData['FICO.Score'] = loansData['FICO.Range']
print loansData['FICO.Score'][0:5]
A =loansData['FICO.Score'].tolist()
#print (A)
FICO=[] #declare an empty array
for j in range(len(A)):   #for j in between 0 to len(A)
  B = A[j].split("-")     #split each sub-array on - and save it to B
  #C = int(B[0], B[1])    #convert the str to int
  #C = np.mean(C)         #finding the mean of B[0] and B[1]
  C = float(B[0])           #convert the string to int, using only the first value
  FICO.append(C)          #append each C to the empty array, using first value
loansData['FICO.Score']=FICO
print FICO [0:5]


plt.figure()
p = loansData['FICO.Score'].hist()
plt.show()

#scatterplot matrix

a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10))
plt.show()

#plots on the diagonal showing histogram for each variable. 
a=pd.scatter_matrix(loansData, alpha=0.05, figure=(10,10), diagonal='hist')
plt.show()

intrate = loansData ['Interest.Rate']
loanamt = loansData ['Amount.Requested']
fico = loansData['FICO.Score']

# the dependent variable
y = np.matrix(intrate).transpose()
print y

#The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()
print x1

x = np.column_stack([x1,x2])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()


