# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 18:07:02 2024

@author: pc
"""

def find_grades(grades, students):
    """ grades is a dict mapping student names (str) to grades (str)
        students is a list of student names 
    Returns a list containing the grades for students (in the same order) """
    # your code here
    L=[]
    
    for k,v in d.items():
        if k in students:
            
            L.append(v)
    return L
  

d = {'Ana':'B', 'Matt':'C', 'John':'B', 'Katy':'A'}
print(find_grades(d, ['Matt', 'Katy'])) # returns ['C', 'A']
