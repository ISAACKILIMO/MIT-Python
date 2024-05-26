# -*- coding: utf-8 -*-
"""
Created on Sun May 26 11:44:52 2024

@author: pc
"""
# Method 1
lst=[2,3, [9,5,7],6,[5,'ent'],'nine']
ls=[]
print(type(lst))
for i in lst:
    if type(i)!=list:
        ls.append(i)
    elif type(i)== list:
        for t in i:
            ls.append(t)
print(ls)

