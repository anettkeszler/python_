# 15 Data Structure Patterns to solve LeetCode problems

Sources: 
https://www.youtube.com/watch?v=DjYZk8nrXVY

HelloInterview:
https://www.hellointerview.com/learn/code

### 1. Two Pointers Pattern
- **LeetCode Two Pointers Collection**: https://leetcode.com/problem-list/wi7vqqzg/
- This technique refers to using two pointers that start at opposite ends of an array and gradually move towards each other.
- we assign 2 variables(i- j OR start - end) and move them towards each other 
- it reduce O(n2) to O(n) by using 2 indices moving towards each other
- this technique is ideal for avoiding nested loops, reducing time complexity to linear.
- The key is that “two pointers” isn’t one technique, but several sub-patterns:
    - **1.) Opposite Direction (Left ↔ Right pointers)**
        - Two indices start at both ends and move toward each other
        - Typically used on sorted arrays or palindrome checks
    - **2.) Same Direction (Fast–Slow pointers on arrays)**
        - Both pointers move forward, but at different speeds or roles
        - Used for in-place modification
    - **3.) Sliding Window (Dynamic range with two pointers)**
        - A variation of same-direction pointers
        - Maintain a window [l, r]
    - **4.) Fast–Slow Pointers (Cycle detection / linked list)**
        - One pointer moves faster than the other
        - Used for cycle detection or middle finding
        - Core idea: If there’s a cycle → fast meets slow, otherwise → fast reaches end
    - **5.) Linked List Two-Pointer (Gap technique)**
        - Two pointers with a fixed distance between them
        - Move fast n steps first, then move both


### 2. Sliding Window Pattern
- **LeetCode Sliding Window Pattern Collection**: 
- 


       
