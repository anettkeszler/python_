"""
977. Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/description/?envType=problem-list-v2&envId=wi7vqqzg

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""

def sorted_squares(nums: List[int]):
    start, end = 0, len(nums)-1

    result = []
    
    while start <= end:
        if abs(nums[start]) > abs(nums[end]):
            result.append(nums[start] ** 2)
            start += 1
        else:
            result.append(nums[end] ** 2)
            end -= 1

    return result[::-1]

print(sorted_squares([-4,-1,0,3,10])) # --> [0,1,9,16,100]
print(sorted_squares([-7,-3,2,3,11])) # --> [4,9,9,49,121]
