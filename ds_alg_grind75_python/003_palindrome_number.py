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


# OTHER SOLUTIONS:

def isPalindrome_2(num:int):
    if num < 0:
        return False
    return str(num) == str(num)[::-1]

print(isPalindrome_2(121))
print(isPalindrome_2(-121))
print(isPalindrome_2(10))


# Without converting number to string:
def isPalindrome_3(num):
    return True


print(isPalindrome_3(121))
print(isPalindrome_3(-121))
print(isPalindrome_3(10))