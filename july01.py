# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 11:42:46 2024

@author: pc
"""

L = ['abcde', 'm', 'p', 'xyz', '123', '57']
for i in L:
    print(len(i))
    print(i)
    print((round(len(i)//2)))
print([i[((len(i)//2))] for i in L if (len(i)>2)])
