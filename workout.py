# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:00:07 2024

@author: pc
"""

class workout(object):
    def __init__(self, start, end, calories):
        self.start=start
        self.end=end
        self.calories=calories
        self.icon="):"
        self.kind="workout"
    def get_calories(self):
        return self.calories
    def get_start(self):
        return self.start
    def get_end(self):
        return self.end
    def set_calories(self, calories):
        self.calories=calories
    def set_start(self, start):
        self.start=start
    def set_end(self, end):
        self.end=end
        
print(workout.__dict__.keys())
# print()
print(workout.__dict__.values())
