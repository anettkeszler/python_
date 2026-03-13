"""
Practice 10 LeetCode Problems 

387. First Unique Character in a String 
151. Reverse Word in a String
80. Remove Duplicates from Sorted Array II

Implement Str
Longest Substring without repeating characters
75. Sort Colors
88. Merge Sorted Array 
11. Container With Most Water
15. 3Sum 

"""
# 1.) 387. First Unique Character in a String
def first_unique_char_1(input_str: str):
    unique_char_idx = 0

    for idx, char in enumerate(input_str):
        if input_str.count(char) == 1:
            unique_char_idx = idx
            break
        else:
            unique_char_idx = -1
    return unique_char_idx

print("1. First Unique Character in a String:")
print(first_unique_char_1("leetcode")) # 0
print(first_unique_char_1("loveleetcode")) # 2
print(first_unique_char_1("aabb")) # -1


from collections import defaultdict

def first_unique_char2(input: str):

    char_dict = defaultdict(int)

    for char in input:
        char_dict[char] += 1

    for idx, char in enumerate(input):
        if char_dict[char] == 1:
            return idx
    return -1

print()
print(first_unique_char2("leetcode")) # 0
print(first_unique_char2("loveleetcode")) # 2
print(first_unique_char2("aabb")) # -1, if no unique char

from collections import Counter

def first_unique_char3(input: str):
    char_dict = dict(Counter(input))
    
    for idx, char in enumerate(input):
        if char_dict[char] == 1:
            return idx
    return -1

print()
print(first_unique_char3("leetcode")) # 0
print(first_unique_char3("loveleetcode")) # 2
print(first_unique_char3("aabb")) # -1, if no unique char

# 2.) 151. Reverse Word in a String
def reverse_word_ina_string(input_str):
    input_list = " ".join(input_str.split()).split()
    
    start, end = 0, len(input_list)-1

    while start < end:
        input_list[start], input_list[end] = input_list[end], input_list[start]
        start += 1
        end -= 1
    
    return " ".join(input_list)

print()
print("2.) Reverse Word in a String: ")
print(reverse_word_ina_string("the sky is blue")) # "blue is sky the"
print(reverse_word_ina_string("  hello world  ")) # "world hello"
print(reverse_word_ina_string("a good   example")) # "example good a"

# 3.) 80. Remove Duplicates from Sorted Array II
def remove_duplicates_from_sorted_arrayII():
    pass

print()
print("3.) Remove Duplicates from Sorted Array II: ")
