# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 21:22:02 2015

@author: Owner
"""

import collections
testlist = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
c = collections.Counter(testlist)
print c

#number of instances
count_sum = sum(c.values())
for a,b in c.iteritems():
    print "The frequency of number " + str(a) + " is " + str(float(b) / count_sum)
    
import matplotlib.pyplot as plt
x = testlist
plt.boxplot(x)
plt.show()

plt.hist(x, histtype='bar')
plt.show()

import numpy as np 
import scipy.stats as stats
import matplotlib.pyplot as plt

plt.figure()
test_data = np.random.normal(size=1000)   
graph1 = stats.probplot(test_data, dist="norm", plot=plt)
plt.show() #this will generate the first graph


plt.figure()
test_data2 = np.random.uniform(size=1000)
graph2 = stats.probplot(test_data2, dist="norm", plot=plt)
plt.show() #this will generate the second graph