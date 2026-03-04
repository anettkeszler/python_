"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""

# Solution 1 - brute force - nested loop
# time complexity - O(n2) - nested loop check all pairs
# space complexity - O(1) - no extra space is required
# Logic: The inner loop starts at i + 1 to avoid using the same element twice and to prevent checking the same pair twice

def two_sum_bruteforce(nums: List[int], target: int):
    # iterate through each element
    for i in range(len(nums)):
        # iterate through the rest of the elements:
        for j in range(i+1, len(nums)):
            # check if the sum matches the target:
            if nums[i] + nums[j] == target:
                return [i, j]
    return [] # return empty list if no matches found 

print(two_sum_bruteforce(nums = [2,7,11,15], target = 9)) # [0,1]
print(two_sum_bruteforce(nums = [3,2,4], target = 6)) # [1,2]
print(two_sum_bruteforce(nums = [3,3], target = 6)) # [0, 1]

# Solution 2 - hashmap/dictionary
# time complexity - O(n) 
# it is storing visited numbers and their indices in a dictionary while scanning the list once. 
# For each number, calculate its complement (target-number) and check if it exists in the dictionary

def two_sum_with_dict(nums: List[int], target: int):
    # seen stores {value: index}
    seen = {}

    for idx in range(len(nums)):
        current_num = nums[idx]
        # if key-value pair in dict:
        complement = target - current_num
        # If complement exists, return its index and current index
        if complement in seen:
            return [seen[complement], idx]
        # Otherwise, store the current number and index
        seen[current_num] = idx
    return [] # Return empty list if no solution exists

print(two_sum_with_dict(nums = [2,7,11,15], target = 9)) # [0,1]
print(two_sum_with_dict(nums = [3,2,4], target = 6)) # [1,2]
print(two_sum_with_dict(nums = [3,3], target = 6)) # [0, 1]

