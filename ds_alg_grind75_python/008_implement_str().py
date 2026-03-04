"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""

# Solution 1 - find() built-in method
# find() method is a built-in string method used to locate the starting index of the first occurrence of a substring within another string. 
# If the substring is found, it returns the index; if it's not found, it returns -1.

def str_str_find(haystack:str, needle:str):
    return haystack.find(needle)

print(str_str_find("sadbutsad", "sad") == 0)
print(str_str_find("leetcode", "leeto") == -1)
print(str_str_find("hello", "ll") == 2)


# Solution 2 - two pointer 
# nested for loop : outer loop complexity: n, inner loop complexity: n --> n * m
def str_str(haystack:str, needle:str):
    if needle == "":
        return 0
    
    i, j = 0, 0




print(str_str("sadbutsad", "sad") == 0)
print(str_str("leetcode", "leeto") == -1)
print(str_str("hello", "ll") == 2)