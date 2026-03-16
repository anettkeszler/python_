"""
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/description/?envType=problem-list-v2&envId=wi7vqqzg

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

def is_palindrome(input: str):

    # "A man, a plan, a canal: Panama" --> "amanaplanacanalpanama"
    alphanum_input = "".join(filter(str.isalnum, input)).lower()

    start, end = 0, len(alphanum_input)-1

    while start < end:
        if alphanum_input[start] != alphanum_input[end]:
            return False
        start+=1
        end-=1
    return True

print(is_palindrome("A man, a plan, a canal: Panama")) # True
print(is_palindrome("race a car")) # False
print(is_palindrome(" ")) # True

"""
# how to filter alphanumerical characters in a string: 

# 1. list comprehension
alphanum_str = "".join([char for char in s if char.isalnum()]).lower()

# 2. filter
alphanum_input = "".join(filter(str.isalnum, input)).lower()

# 3. for loop
alphanum_str = ""
for char in input:
    if char.isalnum():
        alphanum_str+=char
    
"""
