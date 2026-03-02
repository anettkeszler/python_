"""
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
"""

def reverse_number(num : int):
    reversed_num = 0
    
    if num % 10 == 0:
        return

    return reversed_num


print(reverse_number(123)) # 321
print(reverse_number(-123)) # -321
print(reverse_number(120)) # 21 