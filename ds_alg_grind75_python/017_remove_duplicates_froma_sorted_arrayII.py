"""
80. Remove Duplicates from Sorted Array II
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. 
The relative order of the elements should be kept the same.
Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the 
first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k 
elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""

# this solution does not work, as it dont touch the order of the original list items
from collections import defaultdict
def remove_duplicates_from_a_sorted_array_1(nums: List[int]):
    count = 0
    int_dict = defaultdict(int)

    for i in nums:
        int_dict[i] += 1

    for value in int_dict.values():
        if value <= 2:
            count+= value
        else: 
            count+=2
    return count


print()
print(remove_duplicates_from_a_sorted_array_1([0,0,1,1,1,1,2,3,3])) # 7 - [0,0,1,1,2,3,3,_,_]
print(remove_duplicates_from_a_sorted_array_1([1,1,1,2,2,3])) # 5 - [1,1,2,2,3,_]

def remove_duplicates_from_a_sorted_array_2(nums: List[int]):
    count = 0
    outer = 0
    while outer < len(nums):
        inner = outer + 1
        while inner < len(nums) and nums[inner] == nums[outer]:
            inner+=1
        step = inner-outer
        count += min(step, 2)    
        outer += step
    return count

print()
print("3.) Remove duplicates from a sorted array: ")
print(remove_duplicates_from_a_sorted_array_2([0,0,1,1,1,1,2,3,3])) # 7 - [0,0,1,1,2,3,3,_,_]
print(remove_duplicates_from_a_sorted_array_2([1,1,1,2,2,3])) # 5 - [1,1,2,2,3,_]

