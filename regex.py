# -*- coding: utf-8 -*-
"""
Created on Sun May 26 09:27:25 2024

@author: pc
"""
import re

def email_match(email):
    pattern = r"[a-zA-Z.]+@gmail\.com"
    if re.match(pattern, email):
        return "Valid Email Address"
    return "Invalid Email address"

gmail = 'isaackilimo#@gmail.com'
print(email_match(gmail))
