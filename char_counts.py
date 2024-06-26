# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 18:36:01 2024

@author: pc
"""

def char_counts(s):
    """ s is a string of lowercase chars 
    Returns a tuple where the first value is the 
    number of vowels in s and the second value 
    is the number of consonants in s 
    """
    # your code here
    vow=('a','e','i','o','u')
    conso=('b','c','d','f','g','h','j','k','l','m','n','s','p','q','r','t','v','w','x','y','z')
  
    vowel=0
    consonant=0
    lst=[]
    for n in s:
        lst.append(n)
    
    for p in lst:
        if p in vow:
            vowel+=1
        if p in conso:
            consonant+=1
    return (vowel,consonant)


print(f'There are {char_counts("abcd")[0]} vowels and {char_counts("abcd")[1]} consonants')  # prints (1,3)
print(char_counts("zcght"))  # prints (0,5)
print(f'There are {char_counts("zcght")[0]} vowels and {char_counts("zcght")[1]} consonants')