"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0
Explanation:The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1
"""

# With built-in

def firstUniqChar(s: str) -> int:
    char_index = 0
    
    for idx, char in enumerate(s):
        if s.count(char) == 1:
            char_index = idx
            break
        else:
            char_index = -1
    
    return char_index

def firstUniqChar2(s: str): # enhanced version of 1st solution: quick return, updated default value
    for idx, char in enumerate(s):
        if s.count(char) == 1:
            return idx
    return -1

# Without built-in

def firstUniqChar3(s: str) -> int:

    def find(char, idx): # O(N)
        for i in range(len(s)):
            if idx!=i and s[i] == char:
                return True
        return False    

    for idx, char in enumerate(s): # O(N)
        if not find(char, idx): # O(N)
            return idx
    
    return -1

# Optimize algorithm: can we make O(N^2) to O(N)?

def firstUniqChar4(s: str) -> int:
    
    counter = {} # { char: int }

    # pre compute
    for char in s:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

    def unique(char, idx): # O(N) -> O(logN) -> O(1) ?
        return counter[char] == 1
        
    for idx, char in enumerate(s): # O(N)
        if unique(char, idx): # O(1)
            return idx
    
    return -1


def firstUniqChar5(s: str) -> int:
    
    counter = {} # { char: int }

    # pre compute
    for char in s:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

        
    for idx, char in enumerate(s): # O(N)
        if counter[char] == 1: # O(1)
            return idx
    
    return -1

def firstUniqChar6(s: str) -> int:
    # TODO make it with default dict
    # find usage below
    pass

# https://realpython.com/python-counter/
from collections import defaultdict

word = "mississippi"
counter = {}
counter2 = defaultdict(int)

# print(counter["ABCD"])
print(counter2["ABCD"])

for letter in word:
    counter2[letter] = counter2[letter] + 1


def firstUniqChar7(s: str) -> int:
    # TODO make it with the built-in Counter
    # find usage: https://realpython.com/python-counter/
    pass


from collections import Counter
counter = Counter("missisipi")
print(counter)
print(counter['s'])

print(firstUniqChar4("leetcode") == 0 ) # 0
print(firstUniqChar4("loveleetcode") == 2) # 2
print(firstUniqChar4("aabb") == -1) # -1



class MyCounter:
    def __init__(self, s):
        self.counter = {}
    
        for char in s:
            if char in self.counter:
                self.counter[char] += 1
            else:
                self.counter[char] = 1

    def __str__(self):
        return "MyCounter(" + str(self.counter) + ")"

myCounter = MyCounter("missisipi")
print(myCounter)