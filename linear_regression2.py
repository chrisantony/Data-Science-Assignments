# -*- coding: utf-8 -*-
"""
Created on Wed Feb 04 21:36:30 2015

@author: Owner
"""

import pandas as pd
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
y = lambda x: round(float(x.rstrip('%')) / 100, 4)
print y
cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
type(cleanInterestRate)
cleanInterestRate[0:5]
loansData['Interest.Date'] = cleanInterestRate
loansData['Interest.Date'][0:5]
loansData['Loan.Length'][0:5]
cleanLoanLength = loansData['Loan.Length'].map(lambda x: int(x.strip('months')))
cleanLoanLength[0::5]
loansData['Loan.Length'] = cleanLoanLength
loansData['Loan.Length'][0:5]
#to continue with cleaning of FICO RAnge
cleanFICORange = loansData['FICO.Range'].map(lambda x: x.split('-'))
cleanFICORange[1:4].values[0]
type(cleanFICORange[0:5].values[0])
cleanFICORange[0:5].values[0][0]
type(cleanFICORange[0:5].values[0][0])
loansData['FICO.Range'] = cleanFICORange
# Linear Regression Analysis
import numpy as np
import statsmodels.api as sm
intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Range']
y = np.matrix(intrate).transpose()
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()
x = np.column_stack([x1,x2])
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()
print 'Coefficients: ', f.params[0:2]
print 'Intercept: ', f.params[2]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared