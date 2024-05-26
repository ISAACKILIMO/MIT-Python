# -*- coding: utf-8 -*-
"""
Created on Sun May 26 10:26:57 2024

@author: pc
"""

import math

number=123
result=math.sqrt(number)
myans=round(result,2)
print(result)
print(myans)

lst=[3,34,45,67,876,456]
print(lst[2])

a=1
b=2
compare=lambda x,y: x>y
result=compare(a,b)
print(f'{a} is greater than {b}: {result}')