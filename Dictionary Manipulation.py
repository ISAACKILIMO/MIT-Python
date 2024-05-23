# -*- coding: utf-8 -*-
"""
Created on Wed May 22 07:31:32 2024

@author: Kilimo
"""
# #7. Swaps values for Keys in Dictionary
# def swap_keys_values(dict_value):
#     dict2={}
#     for k,v in dict_value.items():
#         dict2[v]=k
#     return dict2
# dict_value={'Ten': 10, 'Twenty':20, 'Thirty':30, 'Forty': 40}
# print(swap_keys_values(dict_value))

# #8. READING A FILE
# def read_content(word):
#     my_dict={}
#     for i in lines:
#         # my_dict[i]=1
#         if i in my_dict:
#             print(i)
#             my_dict[i]+=1
#         else:
#             my_dict[i]=1
#     return my_dict
# with open('australian state of mind.txt', 'r') as file:
#     lines = file.read().lower().split()
#     print(lines)
#     file.close()
# print (read_content(lines))


# #9. Exception Handling

# def exception_handling(lst):
#     try:
#         for i in lst:
#             print( 34/i)
#     except ZeroDivisionError:
#         print ("can't divide by zero")
# lst=[14,7,0,9, 0]
# print(exception_handling(lst))


#10. 