"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
"""

def move_zeroes_twopointer(nums: List[int]):
    next_non_zero = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[next_non_zero], nums[i] = nums[i], nums[next_non_zero]
            next_non_zero += 1
     
     
a_list = [0,1,0,3,12]
move_zeroes_twopointer(a_list) # [1,3,12,0,0]
print(a_list)

b_list = [0]
move_zeroes_twopointer(b_list)
print(b_list)

