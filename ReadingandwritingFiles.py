# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 11:30:26 2015

@author: Owner
"""

with open('C:\Users\Owner\Documents\Thinkful\lecz-urban-rural-population-land-area-estimates_continent-90m.csv') as inputFile:
    header = next(inputFile)
    for line in inputFile:
        line = line.rstrip().split(',')
        line [5] = int(line[5])
        if line[1] == 'Total National Population':
            print line[0], line[5], type(line[5])
            
import collections
population_dict = collections.defaultdict(int)
with open('C:\Users\Owner\Documents\Thinkful\lecz-urban-rural-population-land-area-estimates_continent-90m.csv') as inputFile:
    header = next(inputFile)
    for line in inputFile:
        line = line.rstrip().split(',')
        line [5] = int(line[5])
        if line [1] == 'Total National Population':
            population_dict[line[0]] += line [5]
population_dict
with open('national_population.csv', 'w') as outputFile:
    outputFile.write('continent,2010_population\n')
    for k,v in population_dict.iteritems():
        outputFile.write(k + ',' + str(v) + '\n')

  
from datetime import datetime
print datetime.now()
