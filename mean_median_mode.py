import pandas as pd
import scipy as sp
data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''
data = data.splitlines()
data = [i.split(', ') for i in data]
column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)
from scipy import stats
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)
df['Alcohol'].mean()
df['Alcohol'].median()
stats.mode(df['Alcohol'])


max(df['Alcohol']) - min(df['Alcohol'])
max(df['Tobacco']) - min(df['Tobacco'])
max(df['Alcohol']) - min(df['Alcohol'])
df['Alcohol'].std()
df['Tobacco'].var()
alc_mean = df['Alcohol'].mean()
tob_mean = df['Tobacco'].mean()
print "The mean of the alcohol and tobacco is %.2f, %.2f" %(alc_mean, tob_mean)

#"print" treats the % as a special character you need to add, 
#so it can know, that when you type "f", the number (result) 
#that will be printed will be a floating point type, and the ".2"
# tells your "print" to print only the first 2 digits after the point.