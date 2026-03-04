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

def num_of_digits(x):
    if x == 0:
        return 1
    
    current = abs(x)
    nod = 0 # number of digits
    while current:
        current //= 10
        nod += 1

    return nod

print(num_of_digits(120) == 3)
print(num_of_digits(-120) == 3)
print(num_of_digits(0) == 1)



# 123 =>
# [3, 2, 1] (3)

# 120 =>
# [0, 2, 1] (3)


# 0 * 10**2
# 2 * 10**1
# 1 * 10**0


def reverse_number(num : int):
    reversed_num = 0

    
    while num_of_digits(num):
        # basic case: 1234 --> 4321
        reversed_num = reversed_num * 10 + num % 10 # add the remainder
        num = num // 10 # drop the remainder
        num_of_digits(num) -= 1

    return reversed_num

print(reverse_number(123)) # 321
print(reverse_number(-123)) # -321
print(reverse_number(120)) # 21 

# print(1234 // 10) # 123
# print(1234 % 10) # 4

