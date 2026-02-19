"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric 
characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
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

def is_palindrome(input_string: str):
    alphanum_string = "".join(filter(str.isalnum, input_string))

    start_index = 0
    end_index = len(alphanum_string) - 1

    while start_index < len(alphanum_string) // 2: # in simmetric case, in general cases: while start < end
        if alphanum_string[start_index].lower() != alphanum_string[end_index].lower(): 
            return False
        start_index += 1
        end_index -= 1
            
    return True


print(is_palindrome("racecar"))
print(is_palindrome("A man, a plan, a canal: Panama")) # True
print(is_palindrome("race a car")) # False
print(is_palindrome(" ")) # True

""" 
Source: https://www.geeksforgeeks.org/python/python-remove-all-characters-except-letters-and-numbers/
Explanation:
Remove All Characters Except Letters and Numbers:

1. Using filter() with str.isalnum():

alphanum_string = "".join(filter(str.isalnum, input_string))

- filter() function applies a given condition to each element in an iterable and keeps only those that return True
- str.isalnum() method checks whether a character is alphanumeric (letters or digits)

- filter(str.isalnum, input_string) keeps only characters where isalnum() is True.
''.join() combines the valid characters into a new string


2. Using List Comprehension with str.isalnum():

alphanum_string = "".join([char for char in input_string if char.isalnum()])

- it filters characters efficiently in a single line 
- char.isalnum() returns True for letters and numbers
- only those characters are included and joined into a new string


3. Using for loop:

alphanum_string = ""
for char in input_string:
    if char.isalnum():
        alphanum_string += char
        
"""
