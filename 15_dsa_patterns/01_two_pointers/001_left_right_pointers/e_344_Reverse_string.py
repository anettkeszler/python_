"""
344. Reverse String
https://leetcode.com/problems/reverse-string/description/?envType=problem-list-v2&envId=wi7vqqzg

Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""

def reverse_string(input: List[str]):
    start, end = 0, len(input)-1
    
    while start < end:
        input[start], input[end] = input[end], input[start]
        start += 1
        end-=1
    return input

print(reverse_string(["h","e","l","l","o"])) # --> ["o","l","l","e","h"]
print(reverse_string(["H","a","n","n","a","h"])) # --> ["h","a","n","n","a","H"]

"""
Complexity: 
- time: O(n) - You visit each character at most once, total work grows linearly with the length of the string
- space: O(1) - You modify the array in-place, no extra data structure is created.
"""
 
