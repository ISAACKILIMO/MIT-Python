# -*- coding: utf-8 -*-
"""
Created on Sat May 11 08:18:37 2024

@author: pc
"""
# print no's that have a difference
#import math
def count_nos(i):
    count=0
    count2=0
    eps=0.1
    numbers=''
    Real=i**0.5
    for terms in range(i-10,i+10):
        # print(terms)
       
        if abs(((terms**0.5)-(Real)))<=eps:
        
            count+=1
            numbers=numbers + ' '+str( terms)
        else:
            count2+=1
    print(numbers)
    return count

print(count_nos(100))