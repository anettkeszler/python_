"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

# Source: https://www.youtube.com/watch?v=8u5dz7-96dk

# Solution 1: convert to string
def isPalindrome(num: int):
    str_num = str(num)

    start = 0
    end = len(str_num) -1

    while start < len(str_num) // 2:
        if str_num[start] != str_num[end]:
            return False
        start += 1
        end -= 1
    return True 

print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))


# Solution 2: reverse with sliceing function
def isPalindrome_2(num:int):
    return str(num) == str(num)[::-1]

print(isPalindrome_2(121))
print(isPalindrome_2(-121))
print(isPalindrome_2(10))


# Without converting number to string:
def isPalindrome_3(num):

    if num < 0 or (num % 10 == 0 and num  != 0): # if number less than 0 or number ends with 0 (there is no remainder when we divide by 10) return False
        return False
    
    reversed_num = 0 
    while num > reversed_num: 
        reversed_num = (reversed_num * 10) + (num % 10) # remainder of num divided by 10
        num = num // 10 # drop the last digit
    return num == reversed_num or num == reversed_num//10
        
        
# Explanation: x = 1221 - 12 21- mirrored 
        # we remove the last digit from input number and add it to the reversed_num 
            # reversed_num = 1
            # reversed_num = 12 
        # we repeat it until the half of the number length (if even)


print(isPalindrome_3(121)) 
print(isPalindrome_3(-121))
print(isPalindrome_3(10))
 