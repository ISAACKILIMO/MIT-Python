# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 11:42:46 2024

@author: pc
"""

L = ['abcdefg', 'm', 'p', 'xyz', '123', '57']
for i in L:
    print(len(i))
    print(i)
    print((round(len(i)//2)))
print([i[((len(i)//2))] for i in L if (len(i)>2)])

L1 = [4,5,6]
L=[]
L2 = [1,2,3]   
for i in range(len(L1)):
    print(L1[i])
    print(L2[i])
    test=L.append(L1[i]/L2[i])
    print(L)