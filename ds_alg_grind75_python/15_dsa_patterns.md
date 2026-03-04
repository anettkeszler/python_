# 15 Data Structure Patterns to solve LeetCode problems

Sources: 
https://www.youtube.com/watch?v=DjYZk8nrXVY

HelloInterview:
https://www.hellointerview.com/learn/code

### 1. Two Pointers Pattern
- This technique refers to using two pointers that start at opposite ends of an array and gradually move towards each other.
- we assign 2 variables(i- j OR start - end) and move them towards each other 
- it reduce O(n2) to O(n) by using 2 indices moving towards each other
- this technique is ideal for avoiding nested loops, reducing time complexity to linear.
- Problems:
    - Easy:
        - Valid Palindrome (#125): Check if a string is a palindrome. - DONE
        - Remove Element (#27): In-place removal of elements. 
        - Move Zeroes (#283): Move zeros to the end of an array.
        - Linked List Cycle (#141): Detect cycles in a linked list.
        - Merge Sorted Array (#88): Merge two sorted arrays.
    - Medium:
        - Two Sum II - Input Array Is Sorted (#167): Find two numbers that add up to a target.
        - 3Sum (#15): Find all unique triplets that sum to zero.
        - Container With Most Water (#11): Find two lines that form the most water container.
        - Remove Duplicates from Sorted Array II (#80).
        - Reverse Words in a String (#151).
        - Longest Substring Without Repeating Characters (#3) - (Often used with sliding window).
