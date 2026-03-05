"""
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "bacabcbb"  - bac, ac, cab, abc, bc, b, b 
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:
Input: s = "bbbbb" 
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew" 
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Hint 1
Generate all possible substrings & check for each substring if it's valid and keep updating maxLen accordingly.

"""

# Sliding window

def generate_substrings(input_str: str):
    generated_string_list = []
    return generated_string_list

def length_of_longest_substring(input_str: str):
    next_unique_char = 0

    for i in range(len(input_str)):
        if input_str[i] != input_str[next_unique_char]:
            next_unique_char +=1
    return next_unique_char

        
print(length_of_longest_substring(["bac", "ac", "cab", "abc", "bc", "b", "b" ]))



print(length_of_longest_substring("abcabcbb")) 
print(length_of_longest_substring("bbbbb"))
print(length_of_longest_substring("pwwkew"))



