# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 10:52:12 2024

@author: pc
"""

cube=27
epsilon=0.01
low=0
high=cube
guess=0
num_guess=0

while (guess**3)<=cube:
    guess=guess+epsilon
    high=(low+high)/3
    num_guess+=1
    if guess**3==cube:
        print("The Cube is",guess)
print("The Cuboe is",guess)
print('the number of guesses is',num_guess)