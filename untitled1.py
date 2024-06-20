# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 16:50:16 2024

@author: pc
"""
fileName='lec25_USPopulation.txt'
inFile = open(fileName, 'r')
dates, pops = [], []
for l in inFile:
    print (l)
    line = ''
    for c in l:
        if c in '0123456789 ':
            line += c
print(line)