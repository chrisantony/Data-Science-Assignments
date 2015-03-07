# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 16:49:52 2015

@author: Owner
"""


astr = astr.lower()
newstr = 'a,b,c,d,e'
for i in astr :
    if i not in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~1234567890z ' :
      newstr = newstr + chr(ord(i)+1)
    elif i == 'z':
      newstr = newstr + 'a'
    else:
      newstr = newstr + i
for j in 'aeiou':
    newstr = newstr.replace(j,j.upper())
return newstr  
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print LetterChanges(raw_input())
