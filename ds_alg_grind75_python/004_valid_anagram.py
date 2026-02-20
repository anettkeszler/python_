"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""

def is_anagram(s: str, t: str):
    if sorted(s) == sorted(t):
        return True
    return False

print(is_anagram("anagram", "nagaram")) # True
print(is_anagram("rat", "car")) # False
