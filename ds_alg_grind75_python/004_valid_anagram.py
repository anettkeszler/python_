"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""
# Source of solutions: https://www.youtube.com/watch?v=9UtInBqnCgA&list=PLot-Xpze53lfQmTEztbgdp8ALEoydvnRQ&index=1

# Solution 1
def is_anagram(s: str, t: str):
    return sorted(s) == sorted(t)

print(is_anagram("anagram", "nagaram")) # True
print(is_anagram("rat", "car")) # False

# Solution 2
# HashMap - count the occurances of each characters in both strings
# 1. build the 2 HashMaps: 
#   1.) a: 3, n: 1, g: 1, r: 1, m: 1
#   2.) a: 3, n: 1, g: 1, r: 1, m: 1
# 2. go through the keys and compare the counts for each characters 

# time and memory complexity: O(n) --> O(s+t)

def is_anagram_hashmap(s: str, t: str):
    if len(s) != len(t):
        return False
    
    count_s, count_t = {}, {}
    for i in range(len(s)):
        count_s[s[i]] = 1 + count_s.get(s[i], 0) 
        count_t[t[i]] = 1 + count_t.get(t[i], 0)
    for c in count_s:
        if count_s[c] != count_t.get(c, 0):
            return False
    return True

print(is_anagram_hashmap("anagram", "nagaram"))
print(is_anagram_hashmap("rat", "car"))






