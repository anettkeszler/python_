"""
283. Move Zeroes
https://leetcode.com/problems/move-zeroes/description/?envType=problem-list-v2&envId=wi7vqqzg

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
"""

# 2, 0, 1, 0, 3, 12 
# i            
# k     

def move_zeroes(nums: List(int)):

    non_zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[non_zero] = nums[non_zero], nums[i]
            non_zero += 1
    return nums


print(move_zeroes([0,1,0,3,12])) # [1,3,12,0,0]
print(move_zeroes([0])) # [0]