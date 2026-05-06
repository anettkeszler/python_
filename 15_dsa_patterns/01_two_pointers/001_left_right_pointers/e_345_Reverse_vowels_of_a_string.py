"""
345. Reverse Vowels of a String
https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=problem-list-v2&envId=wi7vqqzg

Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"
Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:
Input: s = "leetcode"
Output: "leotcede"
"""

def reverse_vowels_of_a_string(s: str):
    vowels = "aeiouAEIOU"
    s = list(s) # convert to list (mutable)

    start, end = 0, len(s) -1
    
    while start < end:
    
        while start < end and s[start] not in vowels:
            start += 1
        while start < end and s[end] not in vowels:
            end -= 1
        
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1

    return "".join(s)
        
print(reverse_vowels_of_a_string("IceCreAm")) # --> "AceCreIm"
print(reverse_vowels_of_a_string("leetcode")) # --> "leotcede"


def reverse_vowels_of_a_string2(s: str):
    vowels = "aeiouAEIOU"
    s = list(s)
    
    start, end = 0, len(s)-1

    while start < end:
        if s[start] not in vowels:
            start+=1
        elif s[end] not in vowels:
            end-=1
        else:
            s[start], s[end] = s[end], s[start]
            start+=1
            end -= 1
    
    return "".join(s)

print(reverse_vowels_of_a_string2("IceCreAm")) # --> "AceCreIm"
print(reverse_vowels_of_a_string2("leetcode")) # --> "leotcede"