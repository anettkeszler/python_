"""
Write two Python functions to find the minimum number in a list. 
The first function should compare each number to every other number on the list O(n2). 
The second function should be linear O(n).
"""

# Find min number in a list with O(n)
def find_min_nestedloop(input_list: List[int]):
    min_num = input_list[0]
    
    for i in range(len(input_list)):
        current = input_list[i]
        if current < min_num:
            min_num = current
        
    return min_num

print(find_min_nestedloop([3, 4, 7, 9, 23, 87, 2, 1])) # 1

"""
In Terms of Big O Notation:
One string is an anagram of another if the second is simply a rearrangement of the first. 
For example, heart and earth are anagrams. The strings python and typhon are anagrams as well. 
For the sake of simplicity, we will assume that the two strings in question are of equal length and 
that they are made up of symbols from the set of 26 lowercase alphabetic characters. 
Our goal is to write a boolean function that will take two strings and return whether they are anagrams.
"""

# Solution 1 - built-in sorted(str) function and compare - n^2
def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

print(is_anagram("apple", "pleap"))  # expected: True
print(is_anagram("abcd", "dcba"))  # expected: True
print(is_anagram("abcd", "dcda"))  # expected: False


# Solution 2 - count characters and compare - dictionary - O(2n) --> O(n)
# Although this solution is able to run in linear time, it could only do so by using additional storage 
# to keep the two lists of character counts. In other words, this algorithm sacrificed space in order to gain time.
def is_anagram_dict(s1, s2):
    dict_1 = {}
    dict_2 = {}

    for i in range(len(s1)): # O(n)
        current_char = s1[i]
        if current_char not in dict_1:
            dict_1[current_char] = 1
        else:
            dict_1[current_char] += 1
        # {"a": 1, "p": 2, "l": 1, "e": 1 }

    for j in range(len(s2)): # O(n)
        current_char = s2[j]
        if current_char not in dict_2:
            dict_2[current_char] = 1
        else:
            dict_2[current_char] += 1

    return True if dict_1 == dict_2 else False


print(is_anagram_dict("apple", "pleap"))  # expected: True
print(is_anagram_dict("abcd", "dcba"))  # expected: True
print(is_anagram_dict("abcd", "dcda"))  # expected: False






