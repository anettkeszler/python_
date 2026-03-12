"""
Practice 10 LeetCode Problems on Mondays

125. Valid Palindrome
9. Palindrome Number
245. Valid anagram
344. Reverse String
283. Move Zeroes
1. Two Sum
409. Longest palindrome
167. Two Sum - Sorted Array
7. Reverse Integer 
27. Remove Element 
"""

# 1.) 125. Valid Palindrome
def keep_alphanum_chars(input: str):
    alphanum_str = ""
    for char in input:
        if char.isalnum():
            alphanum_str+= char
    return alphanum_str.lower()

def keep_alphanum_chars2(input: str):
    alphanum_str = "".join([char for char in input if char.isalnum()])
    return alphanum_str.lower()

def keep_alphanum_chars3(input: str):
    alphanum_str = "".join(filter(str.isalnum, input))
    return alphanum_str.lower()

# "A man, a plan, a canal: Panama" --> amanaplanacanalpanama

def is_palindrome(input_str):
    alphanum_str = keep_alphanum_chars3(input_str)

    start = 0
    end = len(alphanum_str) -1

    while start < end:
        if alphanum_str[start] != alphanum_str[end]:
            return False
        start += 1
        end -=1
    return True

print()
print("1. Valid palindrome:")
print(is_palindrome(" ")) # True
print(is_palindrome("A man, a plan, a canal: Panama")) # True
print(is_palindrome("race a car")) # False

# 2.) 9.Palindrome Number
def is_palindrome_number(input_number):
    if input_number < 0 or input_number % 10 == 0: # cover edge cases: negative number or divided by 10
        return False
    
    reversed_number = 0
    while input_number > reversed_number:
        reversed_number = (reversed_number * 10) + input_number % 10 
        input_number //= 10
    return True if reversed_number == input_number or (input_number == reversed_number // 10) else False

print()
print("2. Palindrome number: ")
print(is_palindrome_number(121)) # True
print(is_palindrome_number(-121)) # False
print(is_palindrome_number(10)) # False
print(is_palindrome_number(123321)) # True

# convert to string and reverse with slicing - poor solution but works
def is_palindrome_number2(input_number):
    return str(input_number) == str(input_number)[::-1]

print()
print(is_palindrome_number2(121)) # True
print(is_palindrome_number2(-121)) # False
print(is_palindrome_number2(10)) # False
print(is_palindrome_number2(1234321)) # True

# 3.) 245. Valid anagram

# sorted - poor solution, but works
def is_valid_anagram(input1: str, input2: str):
    return sorted(input1) == sorted(input2)

print()
print("3. Valid anagram: ")
print(is_valid_anagram("anagram", "nagaram")) # True
print(is_valid_anagram("rat", "car")) # False

def is_valid_anagram2(input1: str, input2: str):
    if len(input1) != len(input2):
        return False

    dict1, dict2 = {}, {}

    for i in range(len(input1)):
        current_char = input1[i]
        if current_char not in dict1:
            dict1[current_char] = 1
        else:
            dict1[current_char] += 1

    for i in range(len(input2)):
        current_char = input2[i]
        if current_char not in dict2:
            dict2[current_char] = 1
        else:
            dict2[current_char] += 1
    
    return dict1 == dict2

    # for current_char in dict1:
    #     if current_char not in dict2 or dict1[current_char] != dict2[current_char]:
    #         return False
    #     else:
    #         return True
  
print()
print(is_valid_anagram2("anagram", "nagaram")) # True
print(is_valid_anagram2("rat", "car")) # False

# 4.) 344.Reverse String
# two pointer - best solution
# in-place, O(1)
def reverse_string_two_pointer(input: List[str]):

    start, end = 0, len(input)-1 # chained assignment

    while start < end:
        input[start], input[end] = input[end], input[start]
        start+=1
        end -=1
    return input

print()
print("4. Reverse string: ")
print(reverse_string_two_pointer(["h","e","l","l","o"])) # ["o","l","l","e","h"]
print(reverse_string_two_pointer(["H","a","n","n","a","h"])) # ["h","a","n","n","a","H"]

# slicing - poor solution, but works 
def reverse_string_slicing(input):
    return input[::-1]

print()    
print(reverse_string_slicing(["h","e","l","l","o"])) # ["o","l","l","e","h"]
print(reverse_string_slicing(["H","a","n","n","a","h"])) # ["h","a","n","n","a","H"]

# append, iterate over the array, start at the end
def reverse_string_append(input: List[str]):
    reversed_input = []

    end = len(input)-1

    while end >= 0:
        current_char = input[end]
        reversed_input.append(current_char)
        end -=1
    
    return reversed_input

print()
print(reverse_string_append(["h","e","l","l","o"])) # ["o","l","l","e","h"]
print(reverse_string_append(["H","a","n","n","a","h"])) # ["h","a","n","n","a","H"]

# reversed() function
# reversed() returns an iterator, so it needs to be converted back into a list
def reverse_string_builtin_reversed(input):
    return list(reversed(input))

print()
print(reverse_string_builtin_reversed(["h","e","l","l","o"])) # ["o","l","l","e","h"]
print(reverse_string_builtin_reversed(["H","a","n","n","a","h"])) # ["h","a","n","n","a","H"]


# 5.) 283.Move Zeroes
def move_zeroes(nums: List[int]):
    # if the number is 0, we ignore it
    next_non_zero = 0

    # move all non-zero elements to the left side
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[next_non_zero] = nums[next_non_zero], nums[i]
            next_non_zero +=1
    return nums

print()
print("5. Move Zeroes:")
print(move_zeroes([0,1,0,3,12])) # [1,3,12,0,0]

# 6.) 1.Two Sum
# dictionary 
def two_sum_nestedloop(nums: List[int], target):
    seen = {}

    for idx in range(len(nums)):
        current_num = nums[idx]
        complement = target - current_num # 7 = 9 - 2 

        if complement in seen:
            return [seen[complement], idx]
        seen[current_num] = idx
    
print()
print("6. Two Sum: ")
print(two_sum_nestedloop([4, 3, 2, 7, 1, 9, 15], target = 9)) # [2, 3]
print(two_sum_nestedloop(nums = [2,7,11,15], target = 9)) # [0,1]
print(two_sum_nestedloop(nums = [3,2,4], target = 6)) # [1,2]
print(two_sum_nestedloop(nums = [3,3], target = 6)) # [0,1]

# 7.) 409.Longest palindrome
# dictionary
from collections import defaultdict

def longest_palindrome(input_str):
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

print()
print("7. Longest palindrome:")
print(longest_palindrome("abccccdd")) # 7 "dccaccd"
print(longest_palindrome("aa")) # 2
print(longest_palindrome("a")) # 1
print(longest_palindrome("aaabbb")) # 5

# 8.) 167. Two Sum - Sorted Array
def two_sum_sorted_array(numbers: List[int], target: int):
    left, right = 0, len(numbers)-1

    while left < right:
        if numbers[left] + numbers[right] > target:
            right -=1
        if numbers[left] + numbers[right] < target:
            left+=1
        if numbers[left] + numbers[right] == target:
            return [left+1, right+1]
        
 
print()
print("8. Two Sum - Sorted Array:")
print(two_sum_sorted_array(numbers = [2,7,11,15], target = 9)) # [1, 2]
print(two_sum_sorted_array(numbers = [2,3,4], target = 6)) # [1, 3]
print(two_sum_sorted_array(numbers = [-1,0], target = -1)) # [1, 2]

# 9.) 7. Reverse Integer 
def reverse_integer(num: int):
    MIN_INT, MAX_INT = -2**31, 2**31
    reversed_int = 0
    sign = -1 if num < 0 else 1
    num = abs(num)

    for i in range(len(str(num))):
        reversed_int = reversed_int * 10 + (num % 10)
        num //= 10 # 

    # edge case 1: negative integer
    reversed_int *= sign
    if reversed_int <= MIN_INT or reversed_int >= MAX_INT:
        return 0

    return reversed_int 

print()
print("9. Reverse integer:")
print(reverse_integer(-123)) # -321
print(reverse_integer(123)) # 321
print(reverse_integer(120)) # 21
print(reverse_integer(1534236469)) # 0

def reverse_integer2(x: int):
    sign = -1 if x < 0 else 1
    res = int(str(abs(x))[::-1]) * sign
        
    # Step 2: Check for 32-bit integer overflow
    if res < -2**31 or res > 2**31 - 1:
        return 0
            
    return res

print(reverse_integer2(-123)) # -321
print(reverse_integer2(123)) # 321
print(reverse_integer2(120)) # 21
print(reverse_integer2(1534236469)) # 0


# 10) Remove Element
def remove_element(numbers: List[int], value:int):
    j = 0
    for i in range(len(numbers)):
        if numbers[i] != value:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            j += 1
    return len(numbers[:j])

print()
print("10. Remove element: ")
print(remove_element(numbers = [3,2,2,3], value = 3)) # 2, nums = [2,2,_,_]
print(remove_element(numbers = [0,1,2,2,3,0,4,2], value = 2)) # 5, nums = [0,1,4,0,3,_,_,_]











