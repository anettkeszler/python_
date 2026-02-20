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

def longestPalindrom(input_string):

    result = ""

    for char in input_string:
        if input_string.count(char) % 2 == 0:
            result += char
    return len(result)+1

print(longestPalindrom("abccccdd")) # 7 (dccaccd)
print(longestPalindrom("a")) # 1

