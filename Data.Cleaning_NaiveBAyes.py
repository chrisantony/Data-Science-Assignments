# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 16:55:44 2015

@author: Owner
"""

import pandas as pd
from os.path import join
import matplotlib.pyplot as plt
df  = pd.read_csv(join('C:\Users\Owner\Documents\Thinkful\ideal_weight.csv'), names=['id', 'sex', 'actual', 'ideal', 'diff'], header=0)
cleandata = df['sex'].map(lambda x: x.rstrip("''"))
df['sex'] = df['sex'].map(lambda x: x.replace("'",""))
print df['sex'] [0:5]
df.columns.values.tolist()
plt.figure()
plt.hist([df['actual']], histtype='bar', stacked=False)
plt.show()
