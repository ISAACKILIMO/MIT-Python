# -*- coding: utf-8 -*-
"""
Created on Sun May 26 12:08:42 2024

@author: pc
"""
import datetime

time_Now=datetime.datetime.now()
past_time=datetime.datetime(2024, 3,14, 12,11, 14)

difference=time_Now-past_time
print(difference)
print(difference.days)
print(difference.microseconds)
print(difference.seconds)