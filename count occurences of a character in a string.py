# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:21:35 2024

@author: bdwye
"""
'''
Description: Write a recursive function that counts the number of times a given character appears in a string.

Function Signature:

python
Copy code
def count_char(s: str, c: str) -> int:
    pass
Sample Inputs and Outputs:

Input: 'banana', 'a'
Output: 3
Input: 'hello', 'l'
Output: 2
Input: 'recursion', 'r'
Output: 2
'''

#my code, which works fine. I don't know why chatGPT says mine doesn't work when it works with their suggested inputs as well as boundary conditions like empty strings.
def count_char(s: str, c: str) -> int:
    count = 0
    if len(s) <= 1:
        if c in s:
            count += 1
    
    else:
        return count_char(s[0],c) + count_char(s[1:],c) 
    
    return count
        
print(count_char('z', 'z'))

#chatGPT code
def count_char(s: str, c: str) -> int:
    if len(s) == 0:
        return 0  # Base case: if the string is empty, return 0
    
    if s[0] == c:
        return 1 + count_char(s[1:], c)  # Add 1 if the character matches and recurse
    else:
        return count_char(s[1:], c)  # Recurse without adding anything if the character doesn't match
