# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:05:51 2024

@author: bdwye
"""

'''
Description: Write a recursive function that returns the reverse of a given string.

Function Signature:


Input: 'hello'
Output: 'olleh'
Input: 'abcd'
Output: 'dcba'
Input: 'a'
Output: 'a'
'''

#my code
def reverse_string(s: str) -> str:
    if len(s) <= 1:
        return s
    else:
        return reverse_string(s[1:]) + s[0]
    
print(reverse_string('hello'))
print(reverse_string('abcd'))
print(reverse_string('a'))