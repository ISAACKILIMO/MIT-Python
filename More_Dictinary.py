# -*- coding: utf-8 -*-
"""
Created on Sat May 18 21:23:24 2024

@author: Kilimo
"""

def compressed(dict1, dict2):
    dict_combined=dict1 | dict2
    return dict_combined
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

print(compressed(dict1, dict2))

