# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 09:31:32 2024

@author: pc
"""

# word="Hello World"
# lst=['John',3,'567',[456]]
# print(word[6])
# print(lst)
# print(lst[:][slice(3,1)])

# t1 = (1, 'two', 3)
# t2 = (t1, 3.25)
# print(t2)
# print(t1 + t2)
# print((t1 + t2))
# print((t1 + t2)[3])
# print((t1 + t2)[2:5])

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)
# squared contains [1, 4, 9, 16, 25]

number = [1, 2, 3, 4, 5]
odd_numbers = list(filter(lambda x: x % 2 != 0, number))
print(odd_numbers)
# odd_numbers contains [1, 3, 5]

print((lambda x: x**2)(6))