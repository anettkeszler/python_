"""
151. Reverse Words in a String
https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=problem-list-v2&envId=wi7vqqzg

Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string. 
"""

def reverse_word_in_a_string(input: str):
    input = input.split()

    start, end = 0, len(input)-1
    while start < end:
        input[start], input[end] = input[end], input[start]
        start+=1
        end-=1
    return " ".join(input)

print(reverse_word_in_a_string("the sky is blue")) #  "blue is sky the"
print(reverse_word_in_a_string("  hello world  ")) # "world hello"
print(reverse_word_in_a_string("a good   example")) # "example good a"