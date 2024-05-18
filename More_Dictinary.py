# -*- coding: utf-8 -*-
"""
Created on Sat May 18 21:23:24 2024

@author: Kilimo
"""

# def compressed(dict1, dict2):
#     dict_combined=dict1 | dict2
#     return dict_combined
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# print(compressed(dict1, dict2))
# def my_dictionary(employees, defaults):
#      my_dict1={}
#      for ele in employees:
#          my_dict1[ele]=defaults
#      return my_dict1
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}

# print(my_dictionary(employees, defaults))
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
ls=[]
for k in sample_dict.keys():
    ls.append(k)
print(ls)