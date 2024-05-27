# -*- coding: utf-8 -*-
"""
Created on Mon May 27 09:01:09 2024

@author: pc
"""

def hello(func):
    def inner():
        print("Hello")
        #func()
    return inner

def name():
    print("Alice")

obj = hello(name)  # Decorating the function 'name'
obj()  # Calls the modified function
