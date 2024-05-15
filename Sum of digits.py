# -*- coding: utf-8 -*-
"""
Created on Wed May 15 15:53:44 2024

@author: bdwye
"""
'''
Problem 1: Sum of Digits
Description: Write a recursive function that calculates the sum of the digits of a non-negative integer.

Function Signature:


Sample Inputs and Outputs:

Input: 12345
Output: 15
Input: 0
Output: 0
Input: 987
Output: 24
'''

#my code
def sum_of_digits(n: int) -> int:
    length = len(str(n))
    
    if length == 1:
        return int(n)
    else:
        return int(str(n)[0]) + sum_of_digits(int(str(n)[1:]))
    
print(sum_of_digits(987))

#chatGPT code
def sum_of_digits(n: int) -> int:
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)