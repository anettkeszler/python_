"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers 
such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] 
where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, 
index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.

Example 1:
Input: numbers = [2,3,7,11,15], target = 18
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
"""

# Solution 1 - brute force - nested loop
# time complexity - O(n2) - nested loop check all pairs
# space complexity - O(1) - no extra space is required
# Logic: The inner loop starts at i + 1 to avoid using the same element twice and to prevent checking the same pair twice

def two_sum_sorted_array_bruteforce(numbers: List[int], target: int):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
    return []

print(two_sum_sorted_array_bruteforce(numbers = [2,7,11,15], target = 9)) # [1,2]
print(two_sum_sorted_array_bruteforce(numbers = [2,3,4], target = 6)) # [1,3]
print(two_sum_sorted_array_bruteforce(numbers = [-1, 0], target = -1)) # [1,3]


# Solution 2 - hashmap/dictionary
# time complexity - O(n) - we scan the list only once
# it is storing visited numbers and their indices in a dictionary while scanning the list once. 
# For each number, calculate its complement (target-number) and check if it exists in the dictionary

def two_sum_sorted_array_dictionary(numbers: List[int], target: int):
    seen = {}

    # {2: 0, 7: 1, 11: 2, 15: 3}, target = 9

    for idx in range(len(numbers)):
        current_number = numbers[idx]
        complement = target - current_number # (7 = 9 - 2)

        if complement in seen:
            return [seen[complement]+1, idx+1]
        seen[current_number] = idx
    return []

print(two_sum_sorted_array_dictionary(numbers = [2,7,11,15], target = 9)) # [1,2]
print(two_sum_sorted_array_dictionary(numbers = [2,3,4], target = 6)) # [1,3]
print(two_sum_sorted_array_dictionary(numbers = [-1, 0], target = -1)) # [1,3]


# Solution 3 - two pointer

## Solution 3.1 
def two_sum_sorted_array_two_pointers(numbers: List[int], target: int):
    left = 0
    right = len(numbers) -1
    
    for idx in range(len(numbers)): # O(n)
        if numbers[left] + numbers[right] == target:
            return [left+1, right+1]
        if numbers[left] + numbers[right] > target:
            right -= 1
        if numbers[left] + numbers[right] < target:
            left += 1
    return []


print(two_sum_sorted_array_two_pointers(numbers = [2,7,11,15], target = 9)) # [1,2]
print(two_sum_sorted_array_two_pointers(numbers = [2,3,4], target = 6)) # [1,3]
print(two_sum_sorted_array_two_pointers(numbers = [-1, 0], target = -1)) # [1,2]


## Solution 3.2. - refactor
def two_sum_sorted_array_two_pointers2(numbers: List[int], target: int):
    left = 0
    right = len(numbers) -1
    
    while left < right: # O(n)
        total = numbers[left] + numbers[right]
        if total == target:
            return [left+1, right+1]
        if total > target:
            right -= 1
        else:
            left += 1
    return []

# Summary 
"""
The two-pointer technique leverages the fact that the input array is sorted to eliminate the number of pairs we consider from O(n2)down to O(n).
The two-pointers start at opposite ends of the array, and represent the pair of numbers we are currently considering.
We repeatedly compare the sum of the current pair to the target, and move a pointer in a way that eliminates unnecessary pairs from our search.
"""

