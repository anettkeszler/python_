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

def move_zeroes(nums: List[int]):
    insert  = 0 # we keep track the non zero elements
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert], nums[i] == nums[i], nums[insert]
            insert += 1


print(move_zeroes([0,1,0,3,12]))
print(move_zeroes([0]))