"""
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Hint: The entire logic for reversing a string is based on using the opposite directional two-pointer approach!
Do not return anything, modify s in-place instead.
"""
# Complexity for all solutions: O(n)

# Sources:
# https://www.codecademy.com/article/how-to-reverse-a-list-in-python#heading-how-to-reverse-a--list-with-a-for-loop
# https://www.youtube.com/watch?v=ryVNYm89K4o

# Solution 1
# Python's built-in reversed() function is another way to reverse the list. 
# However, reversed() returns an iterator, so it needs to be converted back into a list
    # reversed(list): Returns an iterator that traverses the list in reverse order
    # list(): Converts the iterator into a list

def reverseString_reversed(str_list: List[str]):
    rev = list(reversed(str_list))
    return rev

print(reverseString_reversed(["H","a","n","n","a","h"]))

# Solution 2
# This method builds a reversed version of the list using slicing with a negative step.
# original data is preserved, it creates a new list 
def reverseString_slicing(str_list: List[str]):
    rev = str_list[::-1]
    return rev 

print(reverseString_slicing(["H","a","n","n","a","h"]))

# Solution 3 - reverse() in-place
# reverse() method reverses the elements of the list in-place and it modify the original list directly without creating a new list.
# memory-efficient and easy to use
def reverseString_reverse(str_list: List[str]):
    str_list.reverse()
    print(str_list)

reverseString_reverse(["H","a","n","n","a","h"])

# Solution 4
# Recursion 
def reverseString_recursion(list_str: List[str]):
    # Base case: if the list is empty or has one element 

    if len(list_str) <= 1:
        return list_str
    else:
        # Recursive case: reverse the rest of the list and add the first element at the end 
        return reverseString_recursion(list_str[1:]) + [list_str[0]]

print(reverseString_recursion(["H","a","n","n","a","h"]))

# Solution 5
# Two-pointer
def reverseString_twopointer(str_list: List[str]):

    i, j = 0, len(str_list) - 1 # parallell assignment
    while i < j:
        str_list[i], str_list[j] = str_list[j], str_list[i] # swap 
        i+=1
        j-=1
    
    return str_list

print(reverseString_twopointer(["H","a","n","n","a","h"]))





