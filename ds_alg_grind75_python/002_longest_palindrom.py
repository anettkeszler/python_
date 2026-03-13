"""
Given a string s which consists of lowercase or uppercase letters, 
return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

"""
from collections import defaultdict

def longestPalindrom(input_str):
    counts = 0
    char_counts = defaultdict(int)

    # count how many times each character appears - dictionary
    for char in input_str:
        char_counts[char] += 1

    # count how many pairs of characters we have
    for value in char_counts.values():
        if value % 2 == 0:
            counts += value
        else:
            counts += (value-1)
    
    # if there are letters leftovers, use one for the middle
    if counts < len(input_str):
        counts+=1

    return counts 

   
print(longestPalindrom("abccccdd")) # 7 (dccaccd)
print(longestPalindrom("a")) # 1

