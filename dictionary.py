# -*- coding: utf-8 -*-
"""
Created on Sat May 18 08:20:12 2024

@author: Kilimo
"""
# def conversion_to_dic(keys, values):
#     my_dic={}

    
#     for i in keys:
#         for k in values:
#             my_dic[i]=k
#     return my_dic
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# print(conversion_to_dic(keys, values))


# def create_dic(my_list):
#     my_dict={}
#     for i in my_list:
#         for k in range(13):
#             # return None
#             # print(k)
#             my_dict[i]=k
#     return my_dict
# my_list=['January', 'February', 'March', 'April', 'May', 'June','July', 'August','September', 'October', 'November', 'December']
# print(create_dic(my_list))

# def create_dict(my_lst):
#     my_dict = {}
#     for i, month in enumerate(my_lst):
#         my_dict[month] = i
#     return my_dict

# my_lst = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# print(create_dict(my_lst))

# def create_dic(my_list):
#     my_dict = {}
#     for i in range(len(my_list)):
#         month = my_list[i]
#         for k in range(13):
#             my_dict[month] = k
#     return my_dict

# my_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# print(create_dic(my_list))
ls=[]
for i in range(10, 20):
    for k in range(30,40):
        ls.append(i)
        ls.append(k)
print(ls)
