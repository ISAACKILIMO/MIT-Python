# -*- coding: utf-8 -*-
"""
Created on Tue May 21 15:11:33 2024

@author: Kilimo
"""
# 1.Reverse a string word
# def rev_string(string):
#     mylst=string.split()
#     mylist2=[]
#     for i in string:
       
#         mylist2.append(i)
  
#     print(mylist2)
#     mylist3=mylist2[::-1]
    
#     mylist4="".join(mylist3)
#     return mylist4
# string="Hello"
# print(rev_string(string))


#2. FACTORIAL CALCULATION
# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n* fact(n-1)
# print(fact(7))
# print(list("Hello").reverse())

#3. Palindrome
def is_palindrome(word):
    rev_word=list(word)
    my_word=rev_word.copy()
    
    rev_word.reverse()
    reverse=''.join(rev_word)
    if word==reverse:
        return "Word is palindrome"
    else:
        return "word is NOT palindrome"
    # return reverse
word="SISIS"
print(is_palindrome(word))