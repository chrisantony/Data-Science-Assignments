# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 20:00:48 2015

@author: Owner
"""

import pandas as pd
df = pd.read_csv('C:\Users\Owner\Documents\Thinkful\un.csv')
def count_missing(frame):
    return (frame.shape[0] * frame.shape[1]) - frame.count().sum()
df.groupby('country').apply(count_missing)


df.ix[:,['country', 'region']]

df.columns
print(len(df))
y = df.columns.values.tolist()
print y
df['country'].isnull
df[['country', 'region']]