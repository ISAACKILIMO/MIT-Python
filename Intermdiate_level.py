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

# #3. Palindrome
# def is_palindrome(word):
#     rev_word=list(word)
#     my_word=rev_word.copy()
    
#     rev_word.reverse()
#     reverse=''.join(rev_word)
#     if word==reverse:
#         return "Word is palindrome"
#     else:
#         return "word is NOT palindrome"
#     # return reverse
# word="Tattarrattat"
# print(is_palindrome(word.lower()))


# #4. Print words from 1-100
# def div_by_3(n):
#     for i in range (n+1):
#         if i%3==0:
#             print (f"The number: {i} is div by 3, FIZZ")
#         elif i%5==0:
#             print (f"The number: {i} is div by 5, BUZZ")
#         else:
#             pass
# n= 100
# print(div_by_3(n))

#5. Prime number Check
# def is_prime(num):
#     if num <= 1:
#         return False  # Numbers less than or equal to 1 are not prime
#     for i in range(2, num):
#         if (num % i) == 0:
#             break  # If a factor is found, break out of the loop
#     else:
#         return True  # No factors found, so the number is prime
#     return False  # Otherwise, the number is not prime

# # Example usage:
# number_to_check = 29
# if is_prime(number_to_check):
#     print(f"{number_to_check} is a prime number")
# else:
#     print(f"{number_to_check} is not a prime number")

#6. List Comprehension

# def square_no(number):
#     my_result=[x**2 for x in range(1, number+1) if x%2==0]
#     return my_result
# number = 20
# print(square_no(number))

#7. Dictionary Manipulation
def swap_key_values(value):
    my_dict=