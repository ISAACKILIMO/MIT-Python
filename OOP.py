# -*- coding: utf-8 -*-
"""
Created on Thu May 23 12:19:08 2024

@author: pc
"""

class coordinate(object):
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def distance(self, other):
        x_diff_sq=(self.x-self.other)**2
        y_diff_sq=(self.y-self.other)**2
        return (x_diff_sq+y_diff_sq)**0.5
    def origin(self):
        self.x=0
        self.y=0
        
c=coordinate(3, 4)
origin=coordinate(0, 0)
print(f"c of x is{c.x} and origin x is {origin.x}")